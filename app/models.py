from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def hash_password(self):
        self.password = md5(self.password).hexdigest()

    def verify_password(self, password):
        return md5(password).hexdigest() == self.password
