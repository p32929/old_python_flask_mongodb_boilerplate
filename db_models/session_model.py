import mongoengine as me
from mongoengine_mate import ExtendedDocument

from db_models.user_model import Users


class Sessions(ExtendedDocument):
    # name = me.StringField()
    # email = me.StringField()
    # password = me.StringField()
    user = me.ObjectIdField(Users)
    secret = me.StringField()

    meta = {
        'strict': False,
    }
