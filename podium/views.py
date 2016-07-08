# Put all Flask views in here, as suggested by:
# http://flask.pocoo.org/docs/0.11/patterns/packages/
from podium import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")
