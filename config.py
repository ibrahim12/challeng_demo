WTF_CSRF_ENABLED = True
SECRET_KEY = '#sdf2s.!sdf'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
