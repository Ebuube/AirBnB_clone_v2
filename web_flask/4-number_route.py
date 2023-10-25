#!/usr/bin/python3
"""
A simple web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetings():
    """
    Say hello to friends
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """
    Say hello to HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """
    Say hello to C
    """
    old_symbol = "_"
    new_symbol = " "
    try:
        text = str(text)
        text = text.replace(old_symbol, new_symbol)
    except Exception:
        pass
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """
    Say hello to Python
    """
    old_symbol = "_"
    new_symbol = " "
    try:
        text = str(text)
        text = text.replace(old_symbol, new_symbol)
    except Exception:
        pass
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
