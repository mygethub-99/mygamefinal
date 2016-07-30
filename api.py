import time
import endpoints
from protorpc import remote
from protorpc import messages
from protorpc import message_types
from google.appengine.api import taskqueue
from models.messages import(
    StringMessage,
    StringMessage1,
    UserForms,
    ScoreForms
    )
from models.request import (
    checkInventory,
    cancel_game,
    NewGameForm,
    CraftItem,
    GetScore,
    GetUserGame
    )
from models.game import (
    Game, 
    GameForm
    )
from models.user import (
    User,
    ScoreForm,
    UserForm
    )
from models.inventory import Inventory
from dict_list import (
    items, 
    craft, 
    crafty, 
    gamecheck,
    invenOfCraft
    )
from utils import get_by_urlsafe


NEW_GAME_REQUEST = endpoints.ResourceContainer(NewGameForm)
INVENT_CHECK = endpoints.ResourceContainer(checkInventory)
CRAFT_ITEM = endpoints.ResourceContainer(CraftItem)
CANCELED_GAME = endpoints.ResourceContainer(cancel_game)
GAME_HISTORY = endpoints.ResourceContainer \
(urlsafe_game_key=messages.StringField(1))
USER_REQUEST = endpoints.ResourceContainer \
(user_name=messages.StringField(1), email=messages.StringField(2))
GET_USER_GAME = endpoints.ResourceContainer(GetUserGame)
GAMESCORE = endpoints.ResourceContainer(GetScore)


@endpoints.api(name='survive', version='v1')
class SurviveAPI(remote.Service):
    """Game API"""
    
    # Wrap function for user query.
    def query_user(func):
        def query_users(self, request, *args, **kwargs):
            user=User.query(User.name==request.user_name).get()
            return func(self, request, user, *args, **kwargs)
        return query_users      

     
    @endpoints.method(request_message=USER_REQUEST,
                      response_message=StringMessage1,
                      path='user',
                      name='create_user',
                      http_method='PUT')
    def create_user(self, request):
        """Create a User. Requires a unique username"""
        if User.query(User.name == request.user_name).get():
            raise endpoints.ConflictException(
                    'A User with that name already exists!')
        user = User(name=request.user_name, email=request.email)
        #user.put() sends the user info that is ndb
        user.put()
        return StringMessage1(message='User {} created!' \
            .format(request.user_name))

       
    @endpoints.method(request_message=NEW_GAME_REQUEST,
                      response_message=GameForm,
                      path='game',
                      name='new_game',
                      http_method='PUT')
    @query_user
    def new_game(self, request, user):
        """Creates new game"""
        if not user:
            raise endpoints.NotFoundException(
                    'A User with that name does not exist!')
        checklist= [1, 2, 3]
        if (request.how_hard not in checklist):
            raise endpoints.NotFoundException \
            ('Invalid value. Pick a level 1, 2, or 3')
        ingamecheck=Game.query(Game.user==user.key).get()
        if not ingamecheck:
            taskqueue.add(params= \
                {'email': user.email, 'name': user.name},
            url='/tasks/send_newgame_email', method="POST")
            invenlist=self._inventlist(request)
            game=Game.new_game(user.key, request.how_hard)
            return game.to_form \
            ('Prepare to test your survival skills!')

        if ingamecheck.game_over == False:
            raise endpoints.ConflictException \
                ('Only one active game per user is allowed')
        else:
            taskqueue.add(params= \
                {'email': user.email, 'name': user.name},
            url='/tasks/send_newgame_email', method="POST")
            invenlist=self._inventlist(request)
            game=Game.new_game(user.key, request.how_hard)
            return game.to_form \
            ('Prepare to test your survival skills!')

        
    @endpoints.method(request_message=CANCELED_GAME,
                      response_message=StringMessage1,
                      path='cancel',
                      name='cancel_game',
                      http_method='PUT')
    @query_user
    def cancel_game(self, request, user):
        """Cancels game in progress"""
        #user=User.query(User.name==request.user_name).get()
        if not user:
            raise endpoints.NotFoundException(
                    'A User with that name does not exist!')
        #Check to see if use is in a live game.
        ingamecheck=Game.query(Game.user==user.key).get()
        if hasattr(ingamecheck, "user")==True:
            if ingamecheck.game_over==False:
                setattr(ingamecheck, "canceled_game", True)
                setattr(ingamecheck, "game_over", True)
                ingamecheck.put()
                return StringMessage1 \
                (message='User {} has canceled the game. Play again soon!!!'. \
                    format(request.user_name))
            else:
                return StringMessage1 \
                (message='User {} is not in a active game. Game cant be canceled'. \
                    format(request.user_name))
        else:
            raise endpoints.NotFoundException(
                    'User {} does not have any games to cancel!'. \
                    format(request.user_name))
    

    @endpoints.method(request_message=GET_USER_GAME,
                      response_message=GameForm,
                      path='game/get_user_game',
                      name='get_user_game',
                      http_method='POST')
    #Requires POST method to provide request.user.name
    @query_user
    def get_user_game(self, request, user):
        """Return all User's active games"""
        if not user:
            raise endpoints.NotFoundException(
                    'A User with that name does not exist!')
        ingamecheck=Game.query(Game.user==user.key).get()
        if not ingamecheck:
            raise endpoints.NotFoundException('User does not have any games.')
        if ingamecheck.game_over == False:
            return ingamecheck.to_form \
            ('Here is the status of your active game.')
        else:
            raise endpoints.NotFoundException \
            ('No active game found for user. Please try another user name')


    @endpoints.method(request_message=CRAFT_ITEM,
                      response_message=StringMessage1,
                      path='craft',
                      name='craft_item', 
                      http_method='PUT')
    @query_user
    def craftItemNew(self, request, user):
        """Craft an item"""
        if not user:
            raise endpoints.NotFoundException(
                    'A User with that name does not exist!')
        ingamecheck=Game.query(Game.user==user.key).filter \
        (Game.game_over == False)
        ingamecheck =ingamecheck.get()
        if not ingamecheck:
            raise endpoints.NotFoundException \
            ('User is not in a game. Please create a new game for this user.')
        #Check for if out of time.
        if ingamecheck.timeout == True:
            setattr(ingamecheck, "game_over", True)
            ingamecheck.put()
            raise endpoints.ConflictException\
            ('Player has run out of time and did not survive! Start a new game.')
        #Starts the game timer.
        if ingamecheck.game_started == False:
            t1=int(time.time())
            gamediff=getattr(ingamecheck, "difficulty")
            setattr(ingamecheck, "timer", t1)
            setattr(ingamecheck, "game_started", True)
            ingamecheck.put()
        #Calls gamecheck for game timer.
        if ingamecheck.game_started == True:
            if ingamecheck.difficulty > 1:
                gamecheck(ingamecheck)
        # Make a dict of inventory from ndb
        inventory_items=Inventory.query( Inventory.user==user.key)\
        .get()
        # Create a dict of what is needed to craft the item     
        takesToCraft=craft.get(request.itemcraft)
        if takesToCraft == None:
            raise endpoints.NotFoundException('Invalid item name.')
        # Make a copy of takesToCraft to re-populate with ndb values.
        copycraft=takesToCraft.copy()
        #Calls a function to populate copycraft with actual inventory 
        #values from the Inventory ndb model.
        invenOfCraft(copycraft, inventory_items)
        #return of invenOfCraft function.
        inven_ndb=copycraft
        #Compares what is needed to craft an item to what exist in inventory.
        #Determines if required items are present in inventory.
        #Flags True or Fales.
        #Returns message to user if insufficent items in inventory to craft an item.
        canBeMade=True
        for i in craft[request.itemcraft]:
            if craft[request.itemcraft] [i]>inven_ndb[i]:
                canBeMade=False
                return StringMessage1 \
                (message='Sorry, item can not be crafted. Takes {}, you only have {}' \
                    .format(takesToCraft, inven_ndb))
        if canBeMade==True:
            # Adds 1 to the quantity of a crafted item in ndb model.
            increment=1+getattr(inventory_items, request.itemcraft)
            setattr(inventory_items, request.itemcraft, increment)
            #Decrement inventory items used to craft a new item.
            neededForCraft= takesToCraft.copy()
            for w in neededForCraft:
                if hasattr(inventory_items, w)==True:
                    setattr(inventory_items, w, getattr \
                        (inventory_items, w)-neededForCraft[w])
            inventory_items.put()
            ingamecheck.history.append(request.itemcraft)
            ingamecheck.put()
        #Checks to see if you have survived and won the game.
        if inventory_items.tent>=1 and inventory_items.firepit>=1:
            setattr(ingamecheck, "survived", True)
            setattr(ingamecheck, "game_over", True)
            setattr(user, "wins", 1+getattr(user, "wins"))
            setattr(user, "total_played", 1+getattr \
                (user, "total_played"))
            setattr(user, "score", 20*ingamecheck.difficulty+ \
                user.score)
            ingamecheck.put()
            user.put()
            return StringMessage1(message='Congrats {}, you survived! Game over.' \
                .format(inventory_items.name))
        else:
            return StringMessage1(message='{} Can be crafted! {}, You have {}' \
                .format(request.itemcraft, takesToCraft, inven_ndb))
        

    #Pulls a property value of inventory.
    @endpoints.method(request_message=INVENT_CHECK,
                      response_message=StringMessage1,
                      path='invencheck',
                      name='check_items',
                      http_method='POST')
    #Must be POST method to supply request response message
    @query_user
    def checkInventory(self, request, user):
        """Used to pull inventory on a item"""
        chklist=Inventory.query( Inventory.user==user.key).get()
        if not chklist:
            raise endpoints.NotFoundException(
                    'This user does not have any Inventory')
        if user.key==chklist.user:
            itemname=request.item_name
            value=getattr( chklist, itemname)
            return StringMessage1(message='You have {} {} '.format \
                (value, itemname))

 
    #Used by NewGame to check if old inventory list belongs to user,
    #deletes old inventory, creates a new inventory for the user.
    @query_user
    def _inventlist(self, request, user):
        check_invent=Inventory.query(Inventory.name== \
            request.user_name).get()
        #Deletes the inventory list and throw message.    
        if check_invent:
            check_invent.key.delete()
        invent=Inventory(name=user.name, user=user.key, \
            flint=items.get("flint"), grass=items.get("grass"), \
            boulder=items.get("boulder"), hay=items.get("hay"), \
            tree=items.get("tree"), sapling=items.get("sapling"))
        invent.put()
        

    @endpoints.method(message_types.VoidMessage, StringMessage,
            path='howtocraft',
            http_method='GET', 
            name='HowToCraft')
    #Must be a POST method to supply request response message
    def howtoCraft(self, request):
        """Pulls a list of how to craft an item."""
        message=crafty
        return StringMessage(message=message)


    @endpoints.method(request_message=GAME_HISTORY,
                      response_message=StringMessage1,
                      path='game/{urlsafe_game_key}/history',
                      name='game_history',
                      http_method='GET')
    def gameHistory(self, request):
        """Returns the move history of a game"""
        game = get_by_urlsafe(request.urlsafe_game_key, Game)
        if not game:
            raise endpoints.NotFoundException('Game not found')
        return StringMessage1(message=str(game.history))


    @endpoints.method(response_message=UserForms,
                      path='user/ranking',
                      name='get_user_rankings',
                      http_method='GET')
    #Must be POST method to supply request response message
    def get_user_rankings(self, request):
        """Return all Users ranked by their win percentage"""
        users = User.query(User.total_played > 0).fetch()
        users = sorted(users, key=lambda x: x.win_percentage, \
         reverse=True)
        return UserForms(items=[i.to_form() for i in users])


    @endpoints.method(request_message=GAMESCORE,
            response_message=ScoreForms,
            path='user/userscore',
            name='get_high_score',
            http_method='POST')
    #Must be POST method to supply request response message
    def scores(self, request):
        """Present User scores"""
        queryscore = User.query().order(-User.score)
        qscore = queryscore.fetch(request.HowManyToQuery, projection= \
            [User.name, User.score])
        qscore = sorted(qscore, key=lambda x: x.score, reverse=True)
        return ScoreForms(items=[i.to_score() for i in qscore])
         
       
api = endpoints.api_server([SurviveAPI])

