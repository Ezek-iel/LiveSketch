from . import auth_blueprint
from flask import render_template, flash, request, redirect, url_for
from .forms import SignupForm, LoginForm
from ..models import User, db
from ..utilities import strip_errors
from flask_login import login_user, logout_user

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
    if request.method == 'POST':
        if form.validate_on_submit():
            user_to_verify = User.query.filter_by(username = form.username.data).first()
            if user_to_verify:
                if user_to_verify.verify_password(form.password.data):
                    login_user(user_to_verify)
                    flash('Logged in succesfully', 'success')
                    return redirect(url_for('room.all_rooms'))
                else:
                    flash("Username and password is not correct", 'danger')
            else:
                flash('No user with username', 'danger')
        
        if form.errors:
            refined_errors = strip_errors(form.errors)
            flash(refined_errors,'danger' )

    return render_template('auth/login.html', form = form)

@auth_blueprint.route("logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out sucessfully", "success")
    return redirect(url_for('main.home'))