#!/usr/bin/python3
"""
Starts flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """return an html templet that lists all states"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Close a session and start a new session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
