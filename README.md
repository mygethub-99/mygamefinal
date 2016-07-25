# Fullstack Nano Degree Project 6

****

## Name of Project: Survive GAE game api

### Description: This is a game called Survive that is programed to operate on the GAE platform. This is a single player game that involves a player crafting the needed items to survive against the onslaught of the elements. The game is played using the google api explorer on a firefox web browswer.
***

### Required software and files.

Software:
Clone [mygamefinal] (https://github.com/mygethub-99/mygamefinal/edit/master) on your local machine.
Install [Google_App_Launcher] (https://cloud.google.com/appengine/downloads)
Install [FireFox] (https://www.mozilla.org/en-US/firefox/new/?f=86)

Files
api.py: Main application code handleing api models for game functions

app.yaml: Main GAE application config file that determine GAE project that app resides on.

README.md: You are looking at it.

dict_list.py: Contains supporting code for game function.

models.py: Contains classes related to game forms for input and response messaging.

settings.py: Contains web client that is used for oauth operations.

utils.py: Contains support coding for the application.

engineapp: contains version of app.yaml, index.yaml and main.py files

templates folder: Contain all the .html templates used by the application. flask, jinja are used to render templates from python and to script python within html.
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
 11. After completion of the application launch to GAE, type this url in the firefox browser: http:\\workmanapp-server.appspot.com/_ah/api/explorer, or click this link. [Link] (http:\\workmanapp-server.appspot.com/_ah/api/explorer)
 12. You will now have view of the api explorer as host by the GAE server.

***
### How to play the game.
First you will need to create a user, then a new game. When creating a new game you have 3 levels of difficulty. 1 is easy with no time limt, 2 has a 7 minute time limit, and 3 has a 4 minute time limit to survive.
In order to survive you must create a tent and a working firepit with a torch. You have all the resources needed to craft each item. You will have to figure out what is needed to craft each item. You can use the howToCraft function to see how to build each item.
Scoring is setup as 20 points for level 1 game, 40 points for level 2 game and 60 points for a level 3 game.
***
### List of api.py module functions.

query_user decorator used for user query in various modules

create_user creates a new user in GAE

new_game creates a new game for a user

cancel_game ends a game

get_user_game gives a status of a users game

invenOfCraft is used to craft an item

craftItemNew is the module used to craft an item to survive.

checkInventory will check the inventory for a single item that belongs to a user

_inventlist sets up a new inventory for a user

howtoCraft give a listing of how to craft each item

gameHistory provides a listing of each move made by a player for a particular game

get_user_ranking gives a list of each player and their ranking

scores provides the scores for a variable number of players pulled.


