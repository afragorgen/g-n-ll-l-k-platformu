from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


from routes.main_routes import main
from routes.events import events_bp

app = Flask(__name__)


app.config.from_object(Config)


db = SQLAlchemy(app)

app.register_blueprint(main)
app.register_blueprint(events_bp)

if __name__ == "__main__":
    app.run(debug=True)
