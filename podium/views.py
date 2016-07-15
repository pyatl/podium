# Put all Flask views in here, as suggested by:
# http://flask.pocoo.org/docs/0.11/patterns/packages/
from podium import app
from flask import render_template
from flask_dance.contrib.meetup import meetup


@app.context_processor
def inject_meetup_user():
    """
    Allows templates to get the current user information. This is done specifically so
    the layout template can access this information.

    :return:
    """
    meetup_user = None
    if meetup.authorized:
        resp = meetup.get("member/self")
        assert resp.ok
        meetup_user = resp.json()

    return dict(meetup_user=meetup_user)

@app.route('/')
def index():
    """
    Index view. This will be the primary page people see.
    :return:
    """
    return render_template("index.html")
