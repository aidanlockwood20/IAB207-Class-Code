from crypt import methods
from django.shortcuts import render
from flask import Blueprint, render_template, request, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    if 'email' in session: 
        str = '<h1>Hello ' + session['email'] + '</h1>'
    else:
        str = '<h1>Hello World</h1>'

    return str

@main_bp.route('/login', methods = ['GET', 'POST'])
def login():
    session['email'] = request.values.get('email')

    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
        return 'User logged out.'