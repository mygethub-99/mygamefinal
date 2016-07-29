from protorpc import messages
from google.appengine.ext import ndb


class User(ndb.Model):
    """User profile"""
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    wins = ndb.IntegerProperty(default = 0)
    total_played = ndb.IntegerProperty(default = 0)
    score = ndb.IntegerProperty(default = 0)

    @property
    def win_percentage(self):
        if self.total_played > 0:
            return float(self.wins)/float(self.total_played)
        else:
            return 0

    def to_form(self):
        return UserForm(name=self.name,
                        email=self.email,
                        wins=self.wins,
                        total_played=self.total_played,
                        win_percentage=self.win_percentage)
    def to_score(self):
        return ScoreForm(name=self.name,
                         score=self.score
                         )

class ScoreForm(messages.Message):
    """Return message form for scores"""
    name = messages.StringField(1, required = True)
    score = messages.IntegerField(5, required = True)


class UserForm(messages.Message):
    """User Form"""
    name = messages.StringField(1, required = True)
    email = messages.StringField(2, required = True)
    wins = messages.IntegerField(3, required = True)
    total_played = messages.IntegerField(4, required = True)
    win_percentage = messages.FloatField(5, required = True) 
