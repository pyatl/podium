# This application is to be run from the command line!

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from podium import app
from podium.database import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()