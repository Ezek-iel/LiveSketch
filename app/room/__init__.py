from flask import Blueprint

room_blueprint = Blueprint("room", __name__)

from . import routes