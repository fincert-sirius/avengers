from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(
	__name__,
	template_folder="frontend/templates",
	static_folder="frontend/static",
)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from src import models
from src import routes

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)