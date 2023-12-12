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


@app.route("/number_template/<n>", strict_slashes=False)
def number2(n):
    """
        display something from a html file only if n is a number
    """
    if n.isnumeric():
        return flask.render_template("5-number.html", n=n)
    else:
        flask.abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
    """
        display different things of an html file depending on the number
        being even or odd
    """

    if n.isnumeric():
        return flask.render_template("6-number_odd_or_even.html", n=int(n))
    else:
        flask.abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
