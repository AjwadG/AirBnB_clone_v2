#!/usr/bin/python3
"""
    0-hello_route module
    first flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ the home route """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
