from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

CsrfProtect(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import views, models
