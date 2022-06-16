from audioop import add
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField

class UserForm(FlaskForm):
    first_name = StringField("Enter first name")
    last_name = StringField("Enter last name")
    email_address = StringField("Enter your email address")
    phone_number = StringField("Enter your phone number")
    submit = SubmitField ("Submit")

class ReviewForm(FlaskForm):
    user_id = SelectField ("users", choices=[])
    movie_name= StringField("Enter the movie name")
    genre = SelectField("Genre", choices=[
        ("action", "Action"), 
        ("horror", "Horror"), 
        ("thriller", "Thriller"),
        ("comedy", "Comedy"), 
        ("romance", "Romance"), 
        ("scifi", "Sci-fi"),
        ("other", "Other")
        ])
    review_description= StringField("Enter your review of the movie (Max 750 words)")
    review_rating = StringField ("Enter your rating off the move out of 10")
    date_watched = DateField("Enter the date you watched the movie")
    submit = SubmitField ("Submit your review")    
    