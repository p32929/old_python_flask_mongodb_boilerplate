from flask import Flask
import certifi
from mongoengine import connect

from db_models.Users import Users

#
app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"


#
def connect_database():
    connect('project1')


connect_database()


@app.route("/")
def hello_world():
    hello_ver = "Hello World"

    i = Users.col().insert_one({
        "name": "F",
        "email": "E",
        "password": "P",
    })

    return hello_ver
