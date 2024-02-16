#!/usr/bin/python3
"""
    3-python_route.py module
    flask app with 4 routes
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


@app.route("/c/<text>", strict_slashes=False)
def c_with_message(text):
    """ the c route that accepts url args """
    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_message(text="is cool"):
    """ the python route that accepts url args """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
