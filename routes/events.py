from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from extensions import db
from models.event import Event
from models.user import User

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
    if not session.get("user_id"):
        flash("Etkinlik oluşturmak için giriş yapmalısınız", "warning")
        return redirect(url_for("auth_bp.login"))

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
            image_url="animal.jpg"  
        )

        db.session.add(new_event)
        db.session.commit()

        flash("Etkinlik başarıyla oluşturuldu", "success")
        return redirect(url_for("events_bp.events"))

    return render_template("event_create.html")


@events_bp.route("/events/<int:event_id>/join")
def join_event(event_id):
    if not session.get("user_id"):
        flash("Katılmak için giriş yapmalısınız", "warning")
        return redirect(url_for("auth_bp.login"))

    event = Event.query.get_or_404(event_id)
    user = User.query.get(session["user_id"])

    if user in event.volunteers:
        flash("Bu etkinliğe zaten katıldınız", "info")
    else:
        event.volunteers.append(user)
        db.session.commit()
        flash("Etkinliğe başarıyla katıldınız 🎉", "success")

    return redirect(url_for("events_bp.event_detail", event_id=event.id))
