#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """Function"""
    storage.close()


@app.route("/states", strict_slashes=False)
def list_of_states():
    """Function"""
    states = storage.all(State).values()
    return render_template(
        "9-states.html", states=states, condition="states_list")


@app.route("/states/<id>", strict_slashes=False)
def list_of_states_id(id):
    """Function"""
    states = storage.all(State)
    # primero verificar que se pase el id
    if id:
        key = "State." + id
        # luego verificar que key(State.421a5..) esté en el diccionario
        if key in states:
            state_id = states[key]
            return render_template(
                "9-states.html", state_id=state_id, condition="state_id")
        else:
            return render_template(
                "9-states.html", condition="not_found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
