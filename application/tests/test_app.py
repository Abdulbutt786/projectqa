from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import User, Review
from flask_sqlalchemy import SQLAlchemy
import pytest


class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app


    def setUp(self):
        db.create_all()
        user_1 = User(first_name = "Abdul", last_name = "Butt", email_address = "abdulbutt123@gmail.com", contact_number = "07432097824")
        review_1 = Review(user_id = 1,movie_name = "Spiderman", genre = "Action",review_description = "Great movie must watch", review_rating = "10" )
        db.session.add(user_1)
        db.session.add(review_1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# user form testing
    def test_user_form(self):
        response = self.client.post(
            url_for('new_user'), 
            data = dict(
                first_name = "Abdul",
                last_name = 'Butt',
                email_address = 'Abdulbutt123@gmail.com',
                phone_number = "07432098294"
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

# review form testing
    def test_review_form(self):
        response = self.client.post(
            url_for('create_review', user_id = 1), 
            data = dict(
                movie_name = 'Spiderman',
                genre = "Action",
                review_description = 'Fantastic movie',
                review_rating = '10',
                user_id = 1
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_review_delete(self):
        response = self.client.get(url_for('delete_review', id = 1))
        self.assertNotIn(b'movie_name', response.data)

class TestViews(TestBase):
# tests home page
    def test_view_home(self):
        response = self.client.get(url_for("index"))
        self.assert200(response)

    def test_view_review(self):
        response = self.client.get(url_for('allreviews', user_id = 1))
        self.assertEqual(response.status_code, 200)

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for('update_review', id = 1),
            data = dict(
                movie_name = "Spiderman3",
                review_rating = "5",
                genre = "Action",
                review_description = "Changed my mine didnt like the ending"

            ),
            follow_redirects = True
        )
        self.assertIn(b"", response.data)

class TestReadUser(TestBase):
    def test_user(self):
        response = self.client.get(
            url_for('new_user', follow_redirects = True,first_name = "", last_name = "", email_address = "", contact_number = ""
        ),data=dict(first_name = "", last_name = "", email_address = "", contact_number = ""))
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)

class TestReadReview(TestBase):
    def test_rev(self):
        response = self.client.get(
            url_for('create_review', follow_redirects = True,user_id = 1, 
        ),data=dict(user_id = "", movie_name = "", genre = "", review_description = "", review_rating = "", date_watched = "" ))
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)
        self.assertIn(b"", response.data)






