from flask import Blueprint, render_template
from models.event import Event

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def list_events():
    events = Event.query.all()
    return render_template("events.html", events=events)
