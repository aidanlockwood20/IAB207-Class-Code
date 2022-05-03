from flask import Blueprint, render_template, request, url_for, redirect
from .forms import DestinationForm

# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    return render_template('destinations/show.html')

@bp.route('/create', methods = ['GET', 'POST'])
def create():

    print('Method Type', request.method)
    form = DestinationForm()
    if form.validate_on_submit():
        print('Successfully Created New Travel Destination', 'Success')
        return redirect(url_for('destination.create'))

    return render_template('destinations/create.html', form = form)