from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.event import Event
from models.participation import Participation

events = Blueprint("events", __name__)

# ETKİNLİK LİSTESİ
@events.route("/events")
def list_events():
    events = Event.query.all()
    return render_template("events.html", events=events)

# ETKİNLİK DETAY
@events.route("/events/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event_detail.html", event=event)

# GÖNÜLLÜ OL
@events.route("/events/<int:event_id>/join", methods=["POST"])
@login_required
def join_event(event_id):
    event = Event.query.get_or_404(event_id)

    already_joined = Participation.query.filter_by(
        user_id=current_user.id,
        event_id=event.id
    ).first()

    if already_joined:
        flash("Bu etkinliğe zaten katıldın.", "warning")
        return redirect(url_for("events.event_detail", event_id=event.id))

    participation = Participation(
        user_id=current_user.id,
        event_id=event.id
    )

    db.session.add(participation)
    db.session.commit()

    flash("Etkinliğe başarıyla katıldın 🎉", "success")
    return redirect(url_for("events.event_detail", event_id=event.id))
