#!/usr/bin/python3
"""
    First flask web app
"""

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
    return ("Hello HBNB!")


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
        Returns C + the string given"
    """
    tex = text.replace("_", " ")
    return (f"C {tex}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
