from flask.ext.wtf import Form
from models import User

from wtforms import  StringField, PasswordField, validators

class RegistrationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=4, max=25)])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25)])

    email = StringField('Email Address', [validators.Email()])

    password = PasswordField('Password', [
        validators.Length(min=6, message='Password length must be greater than 5'),
        validators.EqualTo('password1', message='Passwords must match')
    ])
    password1 = PasswordField('Repeat Password')


    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user != None:
            self.email.errors.append('Email is already in use. Please choose another one.')
            return False

        return True
