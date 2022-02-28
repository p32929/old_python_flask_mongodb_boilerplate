from flask import Blueprint

main_controller = Blueprint('main', __name__)


@main_controller.route('/')
def hello_world():
    return "Hello World"
