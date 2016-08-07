# Fullstack Nano Degree Project 6

****

![logo]:https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjNhLyrpLDOAhXJYyYKHWqgD3YQjRwIBw&url=https%3A%2F%2Fwww.udacity.com%2F&psig=AFQjCNE96vNnj6M3gHUSxPt0egG-XKvdKw&ust=1470692956135437 "Logo Title Text 2"

## Name of Project: Survive GAE game api

### Description: This is a game called "Survive" that is programed to operate on the GAE platform. This is a single player game that involves a player crafting the needed items to survive against the onslaught of the elements. The game is played using the google api explorer. 
***

### Required software and files.

Software:
Clone [mygamefinal] (https://github.com/mygethub-99/mygamefinal.git) onto your local machine.
Install [Google_App_Launcher] (https://cloud.google.com/appengine/downloads)

Files
api.py: Main application code handleing api models for game functions

app.yaml: Main GAE application config file that determine GAE project that app resides on.

README.md: Provides information and instructions related to the app survive.

dict_list.py: Contains supporting code for game function.

models.py: Contains classes related to game forms for input and response http messaging.

settings.py: Contains web client that is used for oauth operations.

cron.yaml: configures cron task timing.

utils.py: process url web safe ProtoBuf messaging.

index.py: Is used to create indexes for entity properties related to queries using properties.

***
## Web Application Setup
 1. Install all software listed above under Software section.
 2. Clone game project as shown in Software section.  
 3. Launch Google App Launch. Click file, add existing application and browse to location of the cloned project you down loaded from github.com. Click Ok. 
 4. Once the application has loaded in Google App Launcher, click on the application under the name column and then click run.
 5. Also click on Logs so that you can view application error messaging.
 6. Now open a web browser and type in this url: localhost:8080/_ah/api/explorer 
 7. There may be some web browser configuration changes needed for GAE to work with your browser. 
 8. Add another tab to your web browser and type in this url: localhost:8001. This will open up the App Engine Console. For more info on the App Engine Console, click on this link. [Click_here] (https://cloud.google.com/appengine/docs/python/tools/using-local-server)
 9. You are now ready to run the application on local host.
 10. To play the game on the GAE server, click on the Stop button in the GAE launcher. Wait for the application to stop, then click on deploy in the GAE launcher. This will upload the game code to the GAE server and give you a log window to view for errors.
 11. After completion of the application launch to GAE, type this url in the web browser: http://gamechanger-1260.appspot.com/_ah/api/explorer, or click this link. [Link] (http://gamechanger-1260.appspot.com/_ah/api/explorer)
 12. You shold now have view of the api explorer as hosted by the GAE server in your web browser.
 13. NOTE: There is an issue with API explorer not displaying api descriptions for api using none-GAE decorators.

***
### How to play the game.
1. Create new user by selecting the survive.create_user link. Input your email address and a unique user name.
2. Create a new game by selecting the survive.new_game link. Choose the level of difficulty of the game 1=easy unlimited game time, 2= a seven minute limit to play the game, 3= a four minute game time limit. A user can only have ONE active game at a time. Game timer does not start ticking until a player crafts their first item
3. To win a player must craft a firepit and a tent. Use the survive.howToCraft link to see what items are needed to craft an item. Each player starts with all the flint, grass, tree, sapling, and boulders needed to make items required to build a tent and a firepit.
* Hints
  
 a. Craft lots and lots of twigs and hay first.
   
 b. Craft enough axe to create the logs needed for the firepit.
   
 c. For the tent make a large number of hay and twigs. Run the HowToCraft function again if needed.
   
 d. The game will tell you if you have created an item. If you don't have the items needed to craft something, the game will tell you what is needed to craft the item.

4. Once a tent, firepit and torch are crafted, the game will tell you have survived.
5. A player will recieve 20 points for a level 1 game, 40 points for a level 2 game, and 60 points for a level 3 game.
6. Good Luck!!!!!

***
### How to quick play the game for testing.

Run in localhost or on the GAE server.

Create 2 or more users with valid email addresses

Create 2 games, one for each user

To quickly win the game use the craft_item api

create 22 hay and 22 twig

create 3 axe

create 3 log

create 1 torch

create 1 firepit

create 1 tent

You should now be told that you have won the game. You player will be awarded points.

Now you can test the scoring, ranking and and other game api's.

Thank you and have a nice day!

***
### Endpoints Definitions:
1. survive.cancel_game. 
  * Path:'cancel'
  * Method:'PUT'
  * Parameters:'user_name'
  * Returns:Message confirming that the user's game has been canceled.
  * Descrip:Queries User entity using request.user.name parameter and updates boolean property of User.cancel_game

2. survive.check_items.
  * Path:'invencheck'
  * Method:'GET'
  * Parameters:'user_name, item_name'
  * Returns:Message contains the inventory for a users item in inventory
  * Descrip:Queries Request body supplies user.name and item.name for query of Inventory entity, then return list of item inventory for a single user.

3. survive.craft_item. 
  * Path:'craft'
  * Method:'PUT'
  * Parameters:'itemcraft, user_name'
  * Returns:Message telling the user that the item can, or can not be crafted based on the user's current inventory of items.
  * Descrip:This is the main api in the game. It starts game timers, checks to see if an item can be crafted, if a game has been won, and updates the Game entity and Inventory entity if necessary.

4. survive.create_user.
  * Path:'user'
  * Method:'POST'
  * Parameters:'email, user_name'
  * Returns:Message telling the user that their user profile has been saved to the User entity.
  * Descrip:This api saves the user.email and user.name properties in User entity.

5. survive.game_history.
  * Path:'game/{urlsafe_game_key}/history'
  * Method:'GET'
  * Parameters:'urlsafe_game_key'
  * Returns:Message containing the list of every item crafted by a user during a game.
  * Descrip:This api returns the history of all items crafted during a players game.

6. survive.get_high_score.
  * Path:'user/userscore'
  * Method:'GET'
  * Parameters:'HowManyToQuery'
  * Returns:Message contains list of player scores in descending order, size of list based on the HowManyQuery input parameter.
  * Descrip: This api list a number of players scores equal to the parameter value.

7. survive.get_user_game.
  * Path:'game/get_user_game'
  * Method:'GET'
  * Parameters:'user_name'
  * Returns:Message return a status of the user game by listing Game entity parameters urlsafe_key, game_over, canceled_game, survived, message, and user_name.
  * Descrip:Returns a stats of a user game.

8. survive.get_user_ranking.
  * Path:'user/rankingg'
  * Method:'GET'
  * Parameters:''
  * Returns:Message returns, email, name, total_played, and win_percentage of each player with a score > 0.
  * Descrip:Returns the ranking based on win_percentage of each player in descending order.

9. survive.howToCraft.
  * Path:'howtoCraft'
  * Method:'GET'
  * Parameters:''
  * Returns:Message returns a list of items and how to craft them
  * Descrip:Helful in showing a player what items are needed to craft something.

10. survive.new_game.
  * Path:'game'
  * Method:'POST'
  * Parameters:'how_hard, user_name'
  * Returns:Message returns a status of game for canceled_game, game_over, message, survived, urlsafe_key, and user_name, telling user to prepare to test your survival skills.

