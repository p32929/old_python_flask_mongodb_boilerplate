from flask import Flask
from utils.database_utils import DatabaseUtils

DatabaseUtils.init_local_db()
app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"


@app.route("/")
def hello_world():
    hello_ver = "Hello World"

    return hello_ver
