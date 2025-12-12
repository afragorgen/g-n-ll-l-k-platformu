from app import app
from extensions import db
from models.event import Event

with app.app_context():


    Event.query.delete()

    e1 = Event(
        title="Hayvan Barınağı Yardımı",
        description="Barınaktaki hayvanlara mama desteği ve temizlik çalışması yapılacaktır.",
        date="2025-02-10",
        location="Trabzon Hayvan Barınağı",
        image_url="/static/images/animal.jpg"
    )

    e2 = Event(
        title="Sokak Temizliği Etkinliği",
        description="Mahallemizi birlikte temizliyoruz. Eldiven ve çöp torbaları sağlanacaktır.",
        date="2025-02-20",
        location="Ortahisar Meydan",
        image_url="/static/images/cleaning.jpg"
    )

    e3 = Event(
        title="Yaşlı Bakım Merkezi Ziyareti",
        description="Yaşlı bakım merkezindeki büyüklerimizi ziyaret edip sohbet edeceğiz.",
        date="2025-03-01",
        location="Ortahisar Yaşlı Bakım Merkezi",
        image_url="/static/images/elderly.jpg"
    )

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print(" Etkinlik verileri başarıyla eklendi.")
