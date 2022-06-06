from pdb import post_mortem
from application import app, db
from application.forms import UserForm
from application.forms import ReviewForm
from application.models import User, Review
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_users = User.query.all()
    return render_template('index.html', all_users = all_users)


@app.route("/allmovierev/<int:user_id>")
def allreviews(user_id):
    submitted_reviews=Review.query.filterby(user_id = user_id).all
    return render_template("usermovierev.html", submitted_reviews= submitted_reviews)

@app.route("/new_user", methods = ["GET", "POST"])
def new_user():
    form = UserForm()
    if request.method == "POST":
        user_details = User(first_name = form.first_name.data, last_name = form.last_name.data, email_address = form.email_address.data, contact_number = form.phone_number.data)
        db.session.add(user_details)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("newuser.html", form = form)

@app.route("/create_review/<user_id>")
def create_review(user_id):
    form= ReviewForm()
    if request.method == "POST":
        review = Review(movie_name= form.movie_name.data, genre_movie=form.genre_movie.data, review_description = form.review_description.data,date_watched_movie = form.date_watched_movie.data)
        db.session.add(review)
        db.session.commit()
    return render_template("create_review.html")





