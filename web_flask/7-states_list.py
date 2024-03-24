#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from models.state import State
from flask import Flask as fl
from flask import render_template as rentem

app = fl(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State)
    temp = states.values()
    idNumb = []
    for k in temp:
        idNumb.append(k.id)
    return rentem("7-states_list.html", listed=temp)


@app.teardown_appcontext
def sessClos(arg=None):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
