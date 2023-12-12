#!/usr/bin/python3
"""First flask web app"""


from flask import Flask
"""Import modules"""
app = Flask(__name__)


"""Create an flsk app"""


"""Create a route"""


@app.route("/", strict_slashes=False)
def hello():
    return ("Hello HBNB!")


"""Run the route"""

app.run(host="0.0.0.0", port="5000")
