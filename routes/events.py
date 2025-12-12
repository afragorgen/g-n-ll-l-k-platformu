from flask import Blueprint, render_template
from models.event import Event

events_bp = Blueprint("events_bp", __name__)

@events_bp.route("/events")
def events():
    event_list = Event.query.all()
    return render_template("events.html", events=event_list)

@events_bp.route("/events/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event_detail.html", event=event)
