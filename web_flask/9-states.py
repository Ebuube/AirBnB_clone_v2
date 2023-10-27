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


@app.route('/states', strict_slashes=False)
def get_states():
    """
    Display only the available states
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, state_id=None)


@app.route('/states/<id>', strict_slashes=False)
def get_state_cities(id):
    """
    Display the states and cities under it
    """
    delim = '.'     # same as that used in the console
    states = storage.all(State)
    state_id = State.__name__ + delim + id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000)
