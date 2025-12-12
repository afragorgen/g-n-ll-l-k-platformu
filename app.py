from flask import Flask
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from models.user import User
from models.event import Event

from routes.main_routes import main
from routes.events import events_bp

app.register_blueprint(main)
app.register_blueprint(events_bp)

if __name__ == "__main__":
    app.run(debug=True)
