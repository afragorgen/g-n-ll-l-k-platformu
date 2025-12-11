import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models.event import Event

with app.app_context():
    e1 = Event(
        title="Hayvan Barınağı Yardımı",
        description="Barınaktaki hayvanlara mama desteği ve temizlik çalışması.",
        date="2025-02-10",
        location="Trabzon Hayvan Barınağı",
        image_url="https://picsum.photos/400/200"
    )

    e2 = Event(
        title="Sokak Temizliği",
        description="Mahallemizi birlikte temizliyoruz, malzemeler sağlanacaktır.",
        date="2025-02-20",
        location="Ortahisar Meydan",
        image_url="https://picsum.photos/400/201"
    )

    e3 = Event(
        title="Yaşlı Bakım Merkezi Ziyareti",
        description="Büyüklerimizle sohbet edip zaman geçiriyoruz.",
        date="2025-03-01",
        location="Ortahisar Yaşlı Bakım Merkezi",
        image_url="https://picsum.photos/400/202"
    )

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print("Etkinlikler başarıyla eklendi!")
