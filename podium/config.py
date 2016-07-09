# This file is our lovely config file. Here we can declare config variables that will be useful to our install.
# we can also pull information from the environment and support our heroku install.
# to do this we simply do the following:
#
#    VARIABLE_NAME = environ.get('VARIABLE_NAME')
#
# this will be read in by the app, and allow the config to beset by environment variables.
from os import environ

# This allows you to name the app. Mostly a test variable.
APP_NAME = environ.get('APP_NAME')


# The API keey to get information from Meetup.com about members and what not.
MEETUP_API_KEY = environ.get('MEETUP_API_KEY')
# The Group this is for. so the PyATL group would be python-atlanta
MEETUP_GROUP_NAME = environ.get('MEETUP_GROUP_NAME')

# the OAUTH2 consumer info so people can log in using Meetup.com
MEETUP_OAUTH2_KEY = environ.get('MEETUP_OAUTH2_KEY')
MEETUP_OAUTH2_SECRET = environ.get('MEETUP_OAUTH2_SECRET')