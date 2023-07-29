
from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    nationality = db.Column(db.String(30))
    destinations = db.relationship('Destination', backref='users')