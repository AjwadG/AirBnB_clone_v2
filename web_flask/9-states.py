#!/usr/bin/python3
"""
    9-states module
    2 route renders a template with dynamic content
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ colses the connectetion """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """
        the states_list route that
        renders all states from storage
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_cities(id):
    """
        the states_list route that
        renders all states from storage
    """
    state = storage.all(State).get("State.{}".format(id))
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
