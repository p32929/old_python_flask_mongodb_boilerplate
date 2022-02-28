from flask import Flask, Response
from services.user_service import UserService

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/users")
def users():
    return Response(UserService.get_users())
