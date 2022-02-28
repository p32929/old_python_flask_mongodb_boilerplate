from flask import Flask

from controllers.main_controller import main_controller
from controllers.users_controller import users_controller

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"

app.register_blueprint(main_controller, url_prefix='/')
app.register_blueprint(users_controller, url_prefix='/users')

# @app.route("/users")
# def users():
#     # UserService.create_user()
#     return JsonResp(UserService.get_users(), 200)
