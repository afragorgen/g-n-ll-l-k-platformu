from datetime import datetime
from extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
