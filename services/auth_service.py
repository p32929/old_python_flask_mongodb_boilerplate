import jwt

from constants import Constants


class AuthService:

    @staticmethod
    def make_access_token(user):
        try:
            return jwt.encode(user, Constants.JWT_SECRET, "HS256")
        except:
            return None

    @staticmethod
    def verify_token(token):
        user = jwt.decode(token, Constants.JWT_SECRET, "HS256")
        return user
