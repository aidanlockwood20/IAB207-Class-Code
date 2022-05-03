from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    
    bootstrap = Bootstrap(app)

    app.secret_key = 'sdgsdoddshipd3r74'
    
    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.bp)
    from . import authentication
    app.register_blueprint(authentication.auth_bp)

    return app

