#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask as fl

app = fl(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    """Greets the user with a welcoming message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNBGreeting():
    """Returns a message on the hbnb route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
