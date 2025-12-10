from flask import Blueprint, render_template

# Blueprint oluşturuyoruz
events_bp = Blueprint('events_bp', __name__)

# /events route'u
@events_bp.route('/events')
def events_page():
    return render_template('events.html')
