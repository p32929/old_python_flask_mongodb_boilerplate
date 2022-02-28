from flask import Blueprint

from services.user_service import UserService
from utils.importants_defs import Responder

users_controller = Blueprint('users', __name__)


@users_controller.route('/')
def root():
    return Responder.ok(UserService.get_users())
