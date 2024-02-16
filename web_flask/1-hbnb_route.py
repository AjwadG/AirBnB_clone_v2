#!/usr/bin/python3
"""
    1-hbnb_route module
    flask app with 2 routes
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ the home route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ the hbnb route """
    return "HBNB"


if __name__ == "__main__":
    app.run()
