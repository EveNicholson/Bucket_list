from app import db

class Destination(db.Model):

    __tablename__ = "List of destinations"

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20))
    city = db.Column(db.String(20))
    date = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    