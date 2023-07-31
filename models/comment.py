from app import db

class Comment(db.Model):

    __tablename__ = "Comment"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    