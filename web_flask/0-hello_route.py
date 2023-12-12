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


app.run(host="0.0.0.0", port="5000")
