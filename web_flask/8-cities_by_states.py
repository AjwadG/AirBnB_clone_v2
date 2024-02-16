#!/usr/bin/python3
"""
    8-states_list module
    1 route renders a template with dynamic content
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ colses the connectetion """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
        the cities_by_states route that
        renders all states adn thir cities from storage
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
