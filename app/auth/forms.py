from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from ..models import User

class SignupForm(FlaskForm):

    def validate_username(self, username_to_validate):
        existing_user = User.query.filter_by(username = username_to_validate.data).first()
        if existing_user:
            raise ValidationError("Username already exists")
    
    def validate_emailaddress(self, email_address_to_validate):
        existing_user = User.query.filter_by(emailaddress = email_address_to_validate.data).first()

        if existing_user:
            raise ValidationError('Email address already exists')
        
    username = StringField(label = "Enter Username", validators = [DataRequired(), Length(min = 8,message= "Minimum length of Username is 8 characters")])
    emailaddress = EmailField(label = "Enter Email Address", validators = [DataRequired(),Length(min  = 10), Email(message="Invalid email address")])
    displayname = StringField(label = "Enter Display Name", validators = [DataRequired(),Length(min = 8,message= "Minimum length of password is 8 characters")])
    password = PasswordField(label = "Enter Password", validators=[DataRequired(),Length(min = 8)])
    password_confirm = PasswordField(label = "Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label = "Sign Up")
        

class LoginForm(FlaskForm):

    username = StringField(label = "Enter Username", validators = [DataRequired(), Length(min = 8, message = "Minimum length of Username is 8 characters")])
    emailaddress = EmailField(label = "Enter Email Address", validators = [DataRequired(),Length(min  = 10), Email(message="Invalid email address")])
    password = PasswordField(label = "Enter Password", validators=[DataRequired(),Length(min = 8)])
    submit = SubmitField(label = "Login")
    