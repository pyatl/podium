from flask import Flask, redirect, url_for
from werkzeug.contrib.fixers import ProxyFix
from flask_dance.contrib.meetup import make_meetup_blueprint

# Make our App
app = Flask(__name__)
#Do the proxy fix for heroku and oauth
app.wsgi_app = ProxyFix(app.wsgi_app)

# Pull in our config
app.config.from_object('podium.config')

# Make our meetup blueprint
meetup_blueprint = make_meetup_blueprint(
    key = app.config.get("MEETUP_OAUTH2_KEY"),
    secret = app.config.get("MEETUP_OAUTH2_SECRET")
)

app.register_blueprint(meetup_blueprint, url_prefix="/login")

import podium.views
