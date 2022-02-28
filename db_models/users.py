import mongoengine as me
from mongoengine_mate import ExtendedDocument

class Users(ExtendedDocument):
    name = me.StringField()
    email = me.StringField()
    password = me.StringField()

    meta = {
        'strict': False,
    }
