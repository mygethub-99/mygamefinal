from protorpc import messages


#Input request for needed to cancel a game in progress
class cancel_game(messages.Message):
    """Used to cancel a game in progress"""
    user_name = messages.StringField(1, required = True)


#Input form for making a new game
class NewGameForm(messages.Message):
    """Used to create a new game"""
    user_name = messages.StringField(1, required = True)
    how_hard = messages.IntegerField(2, required = True)


#Input form for crafting an item
class CraftItem(messages.Message):
    """Used to input crafting request"""
    itemcraft = messages.StringField(2, required = True)
