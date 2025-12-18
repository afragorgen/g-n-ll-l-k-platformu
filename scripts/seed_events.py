import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from extensions import db
from models.event import Event
from models.user import User
from datetime import datetime

def seed_events():
    with app.app_context():

        user = User.query.first()
        if not user:
            print("exit Önce bir kullanıcı oluşturmalısın")
            return

        Event.query.delete()

        events = [
            Event(
                title="Hayvan Barınağı Yardımı",
                description="Barınaktaki hayvanlara mama desteği ve temizlik çalışması.",
                date="2025-02-10",
                location="Trabzon Hayvan Barınağı",
                image_url="animal.jpg",
                created_at=datetime.utcnow(),
                created_by_id=user.id
            ),
            Event(
                title="Sahil Temizliği",
                description="Sahil bölgesinde çevre temizliği yapılacaktır.",
                date="2025-03-05",
                location="Trabzon Sahili",
                image_url="sea.jpg",
                created_at=datetime.utcnow(),
                created_by_id=user.id
            )
        ]

        db.session.add_all(events)
        db.session.commit()
        print(" Event seed işlemi başarılı")

if __name__ == "__main__":
    seed_events()
