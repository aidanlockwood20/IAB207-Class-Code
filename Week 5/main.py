from venv import create
from travel import create_app

if __name__ == '__main__':

    new_app = create_app()
    new_app.run(debug = True)

    @new_app.route('/')
    def index():

        return '<h1>Hello World</h1>'