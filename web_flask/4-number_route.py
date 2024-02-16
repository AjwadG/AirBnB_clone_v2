#!/usr/bin/python3
"""
    4-number_route.py module
    flask app with 5 routes
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
    """
        the python route that accepts url args
        another toute in case no url args
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def only_numbers(n):
    """
        the number route that
        accepts url args only if it anumber
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
