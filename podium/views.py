# Put all Flask views in here, as suggested by:
# http://flask.pocoo.org/docs/0.11/patterns/packages/
from podium import app


@app.route('/')
def index():
    return 'Hello World!'
