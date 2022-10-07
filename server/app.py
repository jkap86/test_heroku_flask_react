from flask import Flask
import os

dir = os.path.dirname(__file__)
app = Flask(__name__, static_folder='../client/build/static',
            static_url_path='')


@app.route('/test')
def test():
    return 'This is a test!!! (API)'


app.route('/')


def index():
    return app.send_static_file('index.html')
