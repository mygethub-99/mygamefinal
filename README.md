# Fullstack Nano Degree Project 6

****

## Name of Project: Survive GAE game api

### Description: This is a game called "Survive" that is programed to operate on the GAE platform. This is a single player game that involves a player crafting the needed items to survive against the onslaught of the elements. The game is played using the google api explorer. Best result if FireFox is used.
***

### Required software and files.

Software:
Clone [mygamefinal] (https://github.com/mygethub-99/mygamefinal.git) onto your local machine.
Install [Google_App_Launcher] (https://cloud.google.com/appengine/downloads)
Install [FireFox] (https://www.mozilla.org/en-US/firefox/new/?f=86)

Files
api.py: Main application code handleing api models for game functions

app.yaml: Main GAE application config file that determine GAE project that app resides on.

README.md: Provides information and instructions related to the app survive.

dict_list.py: Contains supporting code for game function.

models.py: Contains classes related to game forms for input and response http messaging.

settings.py: Contains web client that is used for oauth operations.

utils.py: Contains support coding for the application.

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
 6. Now open FireFox and type in this url: localhost:8080/_ah/api/explorer 
 7. Click on the shield symbol at the far left of the url in the browser and disable protection. This will allow the application to run on your browser
 8. Add another tab to firefox browser and type in this url: localhost:8001. This will open up the App Engine Console. For more info on the App Engine Console, click on this link. [Click_here] (https://cloud.google.com/appengine/docs/python/tools/using-local-server)
 9. You are now ready to run the application on local host.
 10. To play the game on the GAE server, click on the Stop button in the GAE launcher. Wait for the application to stop, then click on deploy in the GAE launcher. This will upload the game code to the GAE server and give you a log window to view for errors.
 11. After completion of the application launch to GAE, type this url in the firefox browser: http://gamechanger-1260.appspot.com/_ah/api/explorer, or click this link. [Link] (http://gamechanger-1260.appspot.com/_ah/api/explorer)
 12. You shold now have view of the api explorer as hosted by the GAE server in your Firefox browser.
 13. NOTE: There is an issue with API explorer not displaying api descriptions for api using none-GAE decorators.

***
### How to play the game.
1. Create new user by selecting the survive.create_user link. Input your email address and a unique user name.
2. Create a new game by selecting the survive.new_game link. Choose the level of difficulty of the game 1=easy unlimited game time, 2= a seven minute limit to play the game, 3= a four minute game time limit. A user can only have ONE active game at a time.
3. To win a player must craft a firepit and a tent. Use the survive.howToCraft link to see what items are needed to craft an item. Each player starts with all the flint, grass, tree, sapling, and boulders needed to make items required to build a tent and a firepit.
* Hints
   a. Craft lots and lots of twigs and hay first.
   b. Craft enough axe to create the logs needed for the firepit.
   c. For the tent make lost of hay and twigs.
   d. The game will tell you if you have created an item. If you don't have the items needed to craft something, the game will tell you what is needed to craft the item.
4. Once a tent, firepit and torch are crafted, the game will tell you have survived.
5. A player will recieve 20 points for a level 1 game, 20 points for a level 2 game and 60 points for a level 3 game.
6. Good Luck!!!!!

### List of game functions that can be executed in api explorer
survive.cancel_game. Cancels game based on a user name.

survive.check_items. Gives a user a means to query the inventory for a single inventory item.

survive.craft_item. Use this function to craft items needed to survive.

survive.create_user. Creates a new user.
survive.game_history. Gives a history of a players moves for a url safe game key. Game key can be found in Datastore Viewer Game entity.

survive.get_high_score. List out scores of users. The number returned score is set by HowManyToQuery input.

survive.get_user_game. Provides a status of a users active game.

survive.get_user_ranking. Returns user ranking in descending order for users with a score greater than 0.

survive.howToCraft. Provides a list of items, and what is needed to craft each item to survive.

survive.new_game. Creates a new game for a user. Only one active game allowed per user.

### List of api.py module functions.

query_user decorator used for user query in various modules

create_user creates a new user in GAE

new_game creates a new game for a user, setups up email reminder in taskqueue

cancel_game ends a game

get_user_game gives a status of a users game


craftItemNew is the module used to craft an item to survive

checkInventory will check the inventory for a single item that belongs to a user

_inventlist sets up a new inventory for a user

howtoCraft give a listing of how to craft each item

gameHistory provides a listing of each move made by a player for a particular game

get_user_ranking gives a list of each player and their ranking if the user has a score to rank

scores provides the scores for a variable number of players pulled


