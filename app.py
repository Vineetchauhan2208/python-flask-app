from flask import Flask 
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Well done! You Successfully deployed your flask app, via Github actions, duniya ki mkc, Now you can start building your app.'

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
