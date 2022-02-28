import jwt

from constants import Constants


class AuthService:

    @staticmethod
    def make_access_token(email: str, fullName: str):
        try:
            return jwt.encode({
                "email": email,
                "fullName": fullName
            }, Constants.JWT_SECRET, "HS256")
        except:
            return None

    @staticmethod
    def verify_token(token):
        user = jwt.decode(token, Constants.JWT_SECRET, "HS256")
        print("")
