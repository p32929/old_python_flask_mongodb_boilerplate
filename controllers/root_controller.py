from flask import Blueprint

from constants import Constants

root_controller = Blueprint('main', __name__)


@root_controller.route('/')
def root():
    return f"Hello from {Constants.APP_NAME}"
