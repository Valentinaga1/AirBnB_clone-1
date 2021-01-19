#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def holberton():
    """Function"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function"""
    return "C %s" % text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_message(text="is cool"):
    """Function"""
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """Function"""
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """Function"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
