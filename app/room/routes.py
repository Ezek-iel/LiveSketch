from . import room_blueprint
from flask import render_template

@room_blueprint.route('/')
def all_rooms():
    return render_template('room/rooms.html')