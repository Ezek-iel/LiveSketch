from . import auth_blueprint
from flask import render_template, flash, request, redirect, url_for
from .forms import SignupForm, LoginForm
from ..models import User, db
from ..utilities import strip_errors

@auth_blueprint.route('signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_to_create = User(username = form.username.data, emailaddress = form.emailaddress.data, displayname = form.displayname.data, password = form.password.data)
            db.session.add(user_to_create)
            db.session.commit()
            flash(message="User created succesfully", category = "success")
            return redirect(url_for('room.all_rooms'))
        
        if form.errors:
            refined_errors = strip_errors(form.errors)
            flash(refined_errors, 'danger')

    return render_template('auth/signup.html', form = form)

@auth_blueprint.route('login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form = form)