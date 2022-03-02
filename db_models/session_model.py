import mongoengine as me
from mongoengine_mate import ExtendedDocument

from db_models.user_model import Users


class Sessions(ExtendedDocument):
    user = me.ObjectIdField(Users)
    secret = me.StringField()

    meta = {
        'strict': False,
    }
