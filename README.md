# Fullstack Nano Degree Project 6

****

## Name of Project: Survive GAE game api

### Description: This is a game called Survive that is programed to operate on the GAE platform. This is a single player game that involves a player crafting the needed items to survive against the onslaught of the elements. The game is played using the google api explorer on a firefox web browswer.
***

### Required software and files.

Software:
Install [mygamefinal] (https://github.com/mygethub-99/mygamefinal/edit/master) on your local machine.
Install [Google App Launcher] (https://cloud.google.com/appengine/downloads)
Install [FireFox] https://www.mozilla.org/en-US/firefox/new/?f=86

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
 1. Install Vagrant. Follow these instructions. [vagrant] (https://www.udacity.com/wiki/ud197/install-vagrant)
 2. Clone this project from Github. [project] (https://github.com/mygethub-99/proj3fullstack) into the vagrant directory. 
 3. Open Git Bash and navigate to the vagrant folder with the proj3fullstack master.py file. The execute vagrant up.
    Once vagrant vm is loaded execute the vagrant ssh command. 
 4. Once in vagrant shell (see step 1 for more details) Type in "python dropallfeb32015.py" this command will drop all tables in the      db. Very important step!
 5. Type in "python dbpopfeb3.py" to load the database with app data.
 6. Type in "python master.py" to launch the web server application.
 7. Now open a chrome web browser and type in http://localhost:5000/restaurant/ to display the restaurant application.
 8. You may explore the web application as a visitor, or login using facebaook or your google account login.
 9. Once you are logged in you may add new restaurants to edit and display in the web server application.
 10. To add pictures of your restaurant you will need to to use the edit restaurant menu page. Remember, you can only edit restaurants   that you have created or have been made the owner of.
 11. User will need to pip install Flask-Excel and plug in, pyexcel-xls, for the excel export feature to work.
 12. Link to [Flask Excel] (http://flask-excel.readthedocs.org/en/latest/)

***
### List of master.py module functions.
Functions login, fbconnect, fbdisconnect, gconnect, creatUser, getUserInfo, getUserID, gdisconnect, and disconnect are used for logging in or out of the application using oauth function via facebook and google.

login_required decorator used to redirect a user to the login page.

restaurantMenuJSON, menuItemJSON, restaurantJSON, and showRestaurantJSON are used to create output to mobile devices.

showRestaurant displays a list of the restaurants.

newRestaurant builds a new restaurant in the database using sqlachemy.

editRestaurant allows the user to values held in the restaurant db table.

deleteRestaurant allows the user to delete a restaurant from the database.

showMenu will query and display the restaurant menu.

showRestCuisine will query on a particular type of cuisine.

newMenuItem will allow the user to build a new menu item that.

editMenuItem will allow the user to edit a menuitem that they are a owner of.

deleteMenuItem allows the user to delete a menu item.

notallowed notifies the user of when they have attempted to edit or delete a web page they do not have rights to access.

exportRest will allow the user to export the Restaurant table to excel from the sqlalchemy db.

customExport gives the coder the option to control the scope of the export.
