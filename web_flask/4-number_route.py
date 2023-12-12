#!/usr/bin/python3
"""
    First flask web app
"""
import flask
from flask import Flask
"""
    Create app flask
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Returns the string "Hello HBNB!"
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello1():
    """
        Returns the string "Hello HBNB!"
    """
    return ("HBNB!")


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
        Returns C + the string given"
    """
    tex = text.replace("_", " ")
    return (f"C {tex}")


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
        Returns C + the string given"
    """
    tex = text.replace("_", " ")
    return (f"Python {tex}")


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """
        Returns C + the string given"
    """
    if n.isnumeric():
        return (f"{n} is a number")
    else:
        flask.abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")