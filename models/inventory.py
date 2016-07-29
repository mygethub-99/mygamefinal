from google.appengine.ext import ndb
from user import User


class Inventory(ndb.Model):
    flint = ndb.IntegerProperty(default = 0)
    grass = ndb.IntegerProperty(default = 0)
    hay = ndb.IntegerProperty(default = 0)
    log = ndb.IntegerProperty(default = 0)
    sapling = ndb.IntegerProperty(default = 0)
    twig = ndb.IntegerProperty(default = 0)
    boulder = ndb.IntegerProperty(default = 0)
    pickaxe = ndb.IntegerProperty(default = 0)
    axe = ndb.IntegerProperty(default = 0)
    firepit = ndb.IntegerProperty(default = 0)
    tent = ndb.IntegerProperty(default = 0)
    torch = ndb.IntegerProperty(default = 0)
    tree = ndb.IntegerProperty(default = 0)
    user = ndb.KeyProperty(required = True, kind='User')
    name = ndb.StringProperty(required = True)
