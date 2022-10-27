#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that displays Hello HBNB! """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    """ Function that displays HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    """ Function that displays "C" followed by the value of the text"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hbnb_3(text):
    """ Function that displays "Python" followed by the value of the text"""
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_4(n):
    """ Function that displays "n is a number" """
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def hbnb_5(n):
    """ Function that displays HTML page """
    return(render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hbnb_6(n):
    """ Function that displays HTML page """
    return(render_template('6-number_odd_or_even.html', n=n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
