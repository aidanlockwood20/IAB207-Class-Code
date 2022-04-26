from flask import Flask

def create_app():
    print(__name__)

    app = Flask(__name__)

    app.secret_key = 'dsgdishodsghk'
    from . import views
    app.register_blueprint(views.main_bp)
    return app