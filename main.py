import logging
import webapp2
from google.appengine.api import mail, app_identity
from google.appengine.ext import ndb
from api import SurviveAPI
from utils import get_by_urlsafe
from models.user import User
from models.game import Game


class SendNewGameEmail(webapp2.RequestHandler):
    def post(self):
        """Send email to user once creating a new game"""
        subject = 'Thank you for playing survivor'
        body = 'Hello {} you have a new game in progress. Enjoy!'.format\
        (self.request.get('name'))
        # This will send test emails, the arguments to send_mail are:
        # from, to, subject, body
        mail.send_mail('noreply@{}.appspotmail.com'.format \
          (app_identity.get_application_id()),
          self.request.get('email'),
          subject,
          body)


class ReminderEmail(webapp2.RequestHandler):
    def get(self):
        """Send a reminder email to players with an aging game"""
        users = User.query(User.email != None)
        for user in users:
            games =Game.query(Game.user == user.key).filter(Game.game_over ==\
                False)
            if games.count() > 0:
                sender = 'noreply@{}.appspotmail.com'.format\
                (app_identity.get_application_id())
                to = user.email
                subject = 'Hello {}, finish your survive game!'.format(user.name)
                body = "Dude, it is time to finish this!!!!!" 
                mail.send_mail(sender, to, subject, body) 
              

app = webapp2.WSGIApplication([
    ('/tasks/send_newgame_email', SendNewGameEmail), ('/cron/send_reminder',\
     ReminderEmail)], debug=True)
