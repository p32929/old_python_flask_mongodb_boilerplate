import mongoengine as me
from mongoengine_mate import ExtendedDocument


class BlockedTokens(ExtendedDocument):
    jti = me.StringField()
    created_at = me.DateTimeField()

    meta = {
        'strict': False,
    }
