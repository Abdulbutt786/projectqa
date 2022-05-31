from application import app, db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.Integer,nullable=False, default="0712345678")
    reveiws = db.relationship("Review", backref="reviewbr")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String(60), nullable = False)
    genre = db.Column(db.String(10), nullable = False)
    review_rating = db.Column(db.String(2), nullable = False)
    review_description = db.Column(db.String(500), nullable = False)
    review_date = db.Column(db.DateTime, nullable = False, default = datetime.now)
    User = db.Column(db.Integer, db.ForeignKey("User.id"), nullable = False)