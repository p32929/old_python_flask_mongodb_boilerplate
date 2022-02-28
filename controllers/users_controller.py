from flask import Blueprint

users_controller = Blueprint('users', __name__)


@users_controller.route('/')
def root():
    return "Hello Users"
