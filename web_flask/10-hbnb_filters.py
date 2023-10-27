#!/usr/bin/python3
"""
A simple web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

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


@app.route('/hbnb_filters', strict_slashes=False)
def set_filters():
    """
    Display the filters
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000)
