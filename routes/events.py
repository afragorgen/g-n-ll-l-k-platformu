from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
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

@events_bp.route("/events/create", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        location = request.form["location"]

        new_event = Event(
            title=title,
            description=description,
            date=date,
            location=location,
            image_url="images/animal.jpg"  # şimdilik sabit
        )

        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for("events_bp.events"))

    return render_template("event_create.html")
