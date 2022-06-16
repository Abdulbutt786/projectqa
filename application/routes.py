from application import app, db
from application.forms import UserForm
from application.forms import ReviewForm
from application.models import User, Review
from flask import render_template, request, redirect, url_for

# home page
@app.route('/')
def index():
    all_users = User.query.all()
    return render_template('index.html', all_users = all_users)

# shows all movies reviews
@app.route("/allmovierev/<int:user_id>")
def allreviews(user_id):
    reviews=Review.query.filter_by(user_id = user_id).all()
    return render_template("allmovierev.html", reviews= reviews)

# creatinguser
@app.route("/new_user", methods = ["GET", "POST"])
def new_user():
    form = UserForm()
    if request.method == "POST":
        user_details = User(first_name = form.first_name.data, last_name = form.last_name.data, email_address = form.email_address.data, contact_number = form.phone_number.data)
        db.session.add(user_details)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("newuser.html", form = form)

# createreview
@app.route("/create_review/<int:user_id>",methods=['GET', 'POST'])
def create_review(user_id):
    form= ReviewForm()
    users= User.query.all()
    for user in users:
        form.user_id.choices.append((user.id, f"{user.first_name} {user.last_name}"))
    if request.method == "POST": 
        review = Review(user_id = form.user_id.data,movie_name= form.movie_name.data, genre=form.genre.data, review_description = form.review_description.data,review_rating = form.review_rating.data,date_watched = form.date_watched.data)
        db.session.add(review)
        db.session.commit()
        # will take the user to all their reviews which will be listed
        return redirect(url_for ("allreviews", user_id = user_id))
    return render_template("create_review.html", form=form)

# deletepage
@app.route("/deletereview/<int:id>")
def delete_review(id):
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("index"))

# updatepage
@app.route('/update_review/<int:id>', methods = ['GET', 'POST'])
def update_review(id):
    review = Review.query.get(id)
    form = ReviewForm()
# gets all the reviews by the id off the user and lists them 
    if request.method == "POST":
        review.movie_name = form.movie_name.data
        review.genre = form.genre.data
        review.review_rating = form.review_rating.data
        review.review_description = form.review_description.data
        review.date_watched = form.date_watched.data
        db.session.commit()
        return redirect(url_for('index'))
    
    form.movie_name.data = review.movie_name
    form.genre.data = review.genre
    form.review_rating.data = review.review_rating
    form.review_description.data = review.review_description
    form.date_watched.data = review.date_watched

    return render_template('create_review.html', form = form)


        













