from flask import Flask

from controllers.root_controller import root_controller
from controllers.users_controller import users_controller

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"

app.register_blueprint(root_controller, url_prefix='/')
app.register_blueprint(users_controller, url_prefix='/users')
