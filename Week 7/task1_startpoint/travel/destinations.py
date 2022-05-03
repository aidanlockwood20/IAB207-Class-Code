from flask import Blueprint, render_template
from .models import Destination, Comment

bp = Blueprint('destination', __name__, url_prefix = '/destinations')

@bp.route('<id>')
def show(id):

    destination = get_destination()
    
    return render_template('destinations/show.html', destination = destination)  

def get_destination():

    destination_desc = 'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.'

    img_url = 'https://media-cdn.tripadvisor.com/media/photo-w/06/64/e9/88/roma.jpg'

    comment = Comment('Username', 'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.', 'January 2017')

    destination = Destination('Italy', destination_desc, img_url, '0.62 EUR')
    destination.set_comments(comment)

    return destination
