import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from extensions import db
from models.event import Event

def seed_events():
    with app.app_context():
        Event.query.delete()
        db.session.commit()

        events = [
            Event(
                title="Sokak Hayvanları Besleme",
                description="Sokak hayvanları için mama dağıtımı yapılacaktır.",
                date="2025-06-01",
                location="Trabzon Merkez",
                
            ),
            Event(
                title="Fidan Dikme Etkinliği",
                description="Doğaya katkı için fidan dikiyoruz.",
                date="2025-06-05",
                location="Maçka",
                
            ),
            Event(
                title="Kan Bağışı",
                description="Kızılay ile ortak kan bağışı organizasyonu.",
                date="2025-06-10",
                location="KTÜ Kampüsü",
                
            ),
            Event(
                title="Kıyı Temizliği",
                description="Sahil temizleme gönüllü etkinliği.",
                date="2025-06-15",
                location="Beşirli Sahili",
                
            ),
            Event(
                title="Çocuklar İçin Kitap Toplama",
                description="İhtiyaç sahibi çocuklar için kitap topluyoruz.",
                date="2025-06-20",
                location="Ortahisar",
                
            )
        ]

        db.session.add_all(events)
        db.session.commit()
        print("✅ Etkinlikler başarıyla eklendi.")

if __name__ == "__main__":
    seed_events()
