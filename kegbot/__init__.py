from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('kegbot')
app.config.from_object('kegbot.settings')
try:
    app.config.from_object('config')
except ImportError:
    pass

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from kegbot import models, views
