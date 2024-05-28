#!/usr/bin/python3
"""
This is a simple Flask web application script.
It starts a Flask web app that listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This function responds to the '/states_list' route and returns a HTML page with a list of all State objects present in DBStorage sorted by name (A->Z).
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_db(error):
    """
    This function removes the current SQLAlchemy Session.
