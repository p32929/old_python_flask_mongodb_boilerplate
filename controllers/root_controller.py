from flask import Blueprint

root_controller = Blueprint('main', __name__)


@root_controller.route('/')
def root():
    return "Hello World"
