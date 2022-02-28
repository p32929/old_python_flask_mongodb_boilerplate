from db_models.Users import Users


class UserService:

    @staticmethod
    def get_users():
        return Users.col().find({})