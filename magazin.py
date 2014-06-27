import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'hello flask!'

app.run()
