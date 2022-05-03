from tokenize import String
from typing import Text
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import InputRequired

class DestinationForm(FlaskForm):

    name = StringField('Country', validators = [InputRequired()])

    description = TextAreaField('Description', validators = [InputRequired()])
    image = StringField('Cover Image', validators = [InputRequired()])
    currency = StringField('Currency', validators = [InputRequired()])
    submit = SubmitField('Create') 

class LoginForm(FlaskForm):

    username = StringField('Username', validators = ([InputRequired()]))
    password = PasswordField('Password', validators = ([InputRequired()]))
    submit = SubmitField('Create') 

class RegisterForm(FlaskForm):

    username = StringField('Username', validators = ([InputRequired()]))
    email = EmailField('Email Address', validators = ([InputRequired()]))
    password1 = PasswordField('Password', validators = ([InputRequired()]))
    password2 = PasswordField('Confirm Password', validators = ([InputRequired()]))
    submit = SubmitField('Create') 