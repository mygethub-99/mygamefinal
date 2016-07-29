from protorpc import messages


#Input form for the Query the Inventory list by a property, ie boulder
class checkInventory(messages.Message):
    user_name = messages.StringField(1, required = True)
    item_name = messages.StringField(2, required = True)


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
    user_name = messages.StringField(1, required = True)
    itemcraft = messages.StringField(2, required = True)

#Input form for ranking users
class GetScore(messages.Message):
    """Used to set number of scores queried"""
    HowManyToQuery = messages.IntegerField(1, required = True)


class GetUserGame(messages.Message):
    """Used to input for get_user_game"""
    user_name = messages.StringField(1, required=True)
