from application import app, db
from application.forms import UserForm
from application.forms import ReviewForm
from application.models import User, Review
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_users = User.query.all()
    return render_template('/index.html',all_users = all_users)