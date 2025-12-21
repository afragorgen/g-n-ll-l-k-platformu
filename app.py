from flask import Flask
from extensions import db, login_manager

from routes.auth import auth_bp
from routes.events import events_bp
from routes.main_routes import main_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
login_manager.init_app(app)

import auth_loader

app.register_blueprint(auth_bp)
app.register_blueprint(events_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
