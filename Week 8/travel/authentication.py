from atexit import register
from django.shortcuts import render
from flask import Blueprint, render_template, request, url_for, redirect
from .forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

@auth_bp.route('/login')
def login():

    form = LoginForm()

    if form.validate_on_submit():
        print('Successfully Logged in User')
        return redirect(url_for('authentication.login'))

    return render_template('authentication/login.html', form = form)


@auth_bp.route('/register')
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        print('Successfully Logged in User')
        return redirect(url_for('authentication.login'))

    return render_template('authentication/register.html', form = form)