from flask import Flask

app = Flask(__name__)

# To check if flask is up and running
@app.route('/')
def home_route():
    return "<small>Flask is Fun </small>"