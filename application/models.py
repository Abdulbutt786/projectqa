from application import app, db
from datetime import datetime
from wtforms.validators import DataRequired


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.Integer,nullable=False, default="0712345678")
    reveiws = db.relationship("Review", backref="reviewbr")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String(60), nullable = False)
    genre = db.Column(db.String(10), nullable = False)
    review_rating = db.Column(db.String(2), nullable = False)
    review_description = db.Column(db.String(500), nullable = False)
    date_watched = db.Column(db.DateTime, nullable = True, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)