from db_models.users import Users


class UserService:

    @staticmethod
    def create_user():
        Users.col().insert_one({
            "name": "FF",
            "email": "EE",
            "password": "PP",
        })

    @staticmethod
    def get_users():
        return list(Users.col().find({}))
