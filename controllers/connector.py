from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from controllers.root_controller import root_controller
from controllers.users_controller import users_controller

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
jwt = JWTManager(app)

app.register_blueprint(root_controller, url_prefix='/')
app.register_blueprint(users_controller, url_prefix='/users')
