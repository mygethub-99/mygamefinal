from protorpc import messages
from user import (
	UserForm,
	ScoreForm
	)


#Response message form for user creation
#Sent by the return StringMessage statement in def create_user
class StringMessage(messages.Message):
    """StringMessage-- outbound (multi) string message"""
    message = messages.StringField(1, repeated = True)


class StringMessage1(messages.Message):
    """StringMessage-- outbound (single) string message"""
    message = messages.StringField(1)


class UserForms(messages.Message):
    """Container for multiple User Forms"""
    items = messages.MessageField(UserForm, 1, repeated = True)


class ScoreForms(messages.Message):
    items = messages.MessageField(ScoreForm, 1, repeated = True)
