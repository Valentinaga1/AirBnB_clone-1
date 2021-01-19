#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """Function"""
    storage.close()


@app.route("/states", strict_slashes=False)
def list_of_states():
    """Function"""
    states = storage.all('State').values()
    return render_template(
        "9-states.html", states=states, condition="states_list")


@app.route("/states<id>", strict_slashes=False)
def list_of_states_id():
    """Function"""
    state_all = storage.all('State')
    try:
        state_id = state_all[id]
        return render_template(
            "9-states.html", state_id=state_id, condition="state_id")
    except Exception:
        return render_template(
            "9-states.html", condition="not_found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
