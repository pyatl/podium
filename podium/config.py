# This file is our lovely config file. Here we can declare config variables that will be useful to our install.
# we can also pull information from the environment and support our heroku install.
# to do this we simply do the following:
#
#    VARIABLE_NAME = environ.get('VARIABLE_NAME')
#
# this will be read in by the app, and allow the config to beset by environment variables.
from os import environ

APP_NAME = environ.get('APP_NAME')