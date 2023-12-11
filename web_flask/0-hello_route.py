#!/usr/bin/python3
"""First flask web app"""


from flask import Flask
app = Flask(__name__)
"""gijkjgfnjn gj jk gj kgs gkg """


@app.route("/", strict_slashes=False)
def hello():
    """Display text"""
    return ("Hello HBNB!")


app.run(host="0.0.0.0", port="5000")
"""dkkkdkdkkd dkkdkd dk k dk d"""
