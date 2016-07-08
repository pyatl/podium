from flask import Flask
app = Flask(__name__)
app.config.from_object('podium.config')



import podium.views
