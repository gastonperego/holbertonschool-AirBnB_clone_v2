#!/usr/bin/python3
"""First flask web app"""


from flask import Flask
"""sja kjs  kasjd akjs dkaj k"""
app = Flask(__name__)
"""sja kjs  kasjd akjs dkaj k"""

"""sja kjs  kasjd akjs dkaj k"""


@app.route("/", strict_slashes=False)
def hello():
    """Display text"""
    return ("Hello HBNB!")


"""sja kjs  kasjd akjs dkaj k"""

app.run(host="0.0.0.0", port="5000")
