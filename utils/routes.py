from flask import Flask, Response
from bson import json_util, ObjectId
from services.user_service import UserService
import json

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"


def JsonResp(data, status: int):
    return Response(json.dumps(data, default=str), mimetype="application/json", status=status)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/users")
def users():
    # UserService.create_user()
    return JsonResp(UserService.get_users(), 200)
