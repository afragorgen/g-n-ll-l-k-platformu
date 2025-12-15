import sys
import os
from datetime import date

# Proje kök dizinini Python path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from extensions import db
from models.event import Event


def seed_events():
    events = [
        Event(
            title="Hayvan Barınağı Yardımı",
            description="Barınaktaki hayvanlara mama desteği ve temizlik çalışması.",
            date="2025-02-10",
            location="Trabzon Hayvan Barınağı",
            image_url="animal.jpg"
        ),
        Event(
            title="Sokak Temizliği Etkinliği",
            description="Mahallemizi birlikte temizliyoruz.",
            date="2025-02-15",
            location="Ortahisar",
            image_url="cleaning.jpg"
        ),
        Event(
            title="Yaşlı Bakım Merkezi Ziyareti",
            description="Yaşlılarımızla sohbet ve destek etkinliği.",
            date="2025-02-20",
            location="Akçaabat",
            image_url="elderly.jpg"
        )
    ]

    db.session.add_all(events)
    db.session.commit()
    print("Seed işlemi başarıyla tamamlandı ✅")


if __name__ == "__main__":
    with app.app_context():
        seed_events()
