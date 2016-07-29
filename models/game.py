from protorpc import messages
from google.appengine.ext import ndb
import pickle


class Game(ndb.Model):
    """Game object"""
    user = ndb.KeyProperty(required=True, kind = 'User')
    game_over = ndb.BooleanProperty(required = True, default = False)
    survived = ndb.BooleanProperty(required = True, default = False)
    canceled_game = ndb.BooleanProperty(required = True, default=False)
    history = ndb.PickleProperty(required = True)
    game_started = ndb.BooleanProperty(required = True, default=False)
    difficulty = ndb.IntegerProperty(required = True, default=1)
    timeout = ndb.BooleanProperty(required = True, default=False)
    timer = ndb.IntegerProperty(required = True, default=0)
    

    @classmethod
    def new_game(cls, user, setdiff):
        """Creates and returns a new game"""
        game = Game(user = user,
                    canceled_game = False,
                    survived = False,
                    game_over = False, 
                    game_started = False, 
                    difficulty = setdiff)
        game.history=[]
        game.put()
        return game

    def to_form(self, message):
        """Returns a GameForm representation of the Game"""
        form = GameForm()
        form.urlsafe_key = self.key.urlsafe()
        form.user_name = self.user.get().name
        form.game_over = self.game_over
        form.canceled_game = self.canceled_game
        form.survived = self.survived
        form.message = message
        return form


class GameForm(messages.Message):
    """GameForm for outbound game state information"""
    urlsafe_key = messages.StringField(1, required = True)
    game_over = messages.BooleanField(2, required = True)
    canceled_game = messages.BooleanField(3, required = True)
    survived = messages.BooleanField(4, required = True)
    message = messages.StringField(5, required=True)
    user_name = messages.StringField(6, required = True)
