from forms import RegistrationForm
from app import app, db
from models import User
from flask import render_template, jsonify

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    form = RegistrationForm()
    return render_template('register.html',
                           title='Home',
                           form=form
    )

@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name  = form.last_name.data,
            email = form.email.data,
            password = form.password.data
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({ 'code' : 200, 'status' : 'success' , 'data' : 'Registration Successfull.' })

    form_errors = {}
    for field, errors in form.errors.items():
        for error in errors:
            title = getattr(form, field).label.text
            form_errors[title] = error

    return jsonify({ 'code' : 400, 'status' : 'failure' , 'data' : form_errors })
