from flask import Flask


def create_app():
    app=Flask(__name__)
    
    #add Blueprints
    from . import destinations
    app.register_blueprint(destinations.bp)

    return app

