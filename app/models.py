from app import db
from uuid import uuid4
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    userId = db.Column(db.String(36), default = uuid4, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    password_hash = db.Column(db.String(200), nullable = False)
    displayname = db.Column(db.String(150), nullable = False)
    emailaddress = db.Column(db.String(150), nullable = False)
    created = db.Column(db.DateTime(), default = datetime.now)
    updated = db.Column(db.DateTime(), nullable = True)
    last_online = db.Column(db.DateTime(), nullable = True)

    rooms = db.relationship("Room", backref = "owner")

    @property
    def password(self):
        raise AttributeError("Cant access password directly")
    
    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)
    
    @property
    def avatar_url(self):
        return "https://ui-avatars.com/api/?name={0}&background=random".format(self.emailaddress)
    
    @avatar_url.setter
    def avatar_url(self, value):
        raise AttributeError("Cant set avatar url")
    
    def verify_password(self, value):
        return check_password_hash(self.password_hash, value)
    
    def update_settings(self):
        self.updated = datetime.now()
    
    def ping(self):
        self.last_online = datetime.now()

class Room(db.Model):
    
    roomId = db.Column(db.String(36), default = uuid4, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    members = db.Column(db.Integer(), default = 1)
    created = db.Column(db.DateTime(), default = datetime.now)
    updated = db.Column(db.DateTime(), nullable = True)
    documentId = db.Column(db.String(), nullable = True)

    ownerId = db.Column(db.ForeignKey('user.userId'), nullable = False)
