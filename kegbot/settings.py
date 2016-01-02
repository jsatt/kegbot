import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'kegbot.db'))
