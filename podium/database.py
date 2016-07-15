from podium import app
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class User(db.Model):
    """
    Our User model.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(24))
    name = db.Column(db.String(60))
    github_name = db.Column(db.String(60))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "#{}: {} - {}".format(self.id, self.name, self.email)


class OAuth(db.Model, OAuthConsumerMixin):
    """
    For handling OAuth Tokens
    """
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

class Event(db.Model):
    """
    Refers to a Meetup.com Event.
    Placeholder for more information in the future.
    """

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.Integer)

    def __init__(self, meetup_id):
        self.meetup_id = meetup_id


class Presentation(db.Model):
    """
    Presentations. Will refer to an Event and a User.
    """

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User,
                            backref=db.backref('presentations', lazy='dynamic'))
