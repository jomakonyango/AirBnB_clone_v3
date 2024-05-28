#!/usr/bin/python3
"""
This is a simple Flask web application script.
It starts a Flask web app that listens on 0.0.0.0, port 5000.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function responds to the '/' route (homepage) and returns 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function responds to the '/hbnb' route and returns 'HBNB'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function responds to the '/c/<text>' route and returns 'C ' followed by the value of the text variable.
    """
    return 'C %s' % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
