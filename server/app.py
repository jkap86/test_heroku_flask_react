from flask import Flask

app = Flask(__name__, static_folder='../client/build', static_url_path='')


@app.route('/test')
def test():
    return 'This is a test!!! (API)'


app.route('/')


def index():
    return app.send_from_directory('../client/index.html')
