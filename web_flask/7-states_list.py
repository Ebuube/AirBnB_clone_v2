#!/usr/bin/python3
"""
A simple web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Close connection
    """
    if error is not None:
        print("An error occured:", error)
    else:
        storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    Display the available states
    """
    states = storage.all(State)
    states = [val for val in states.values()]
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
