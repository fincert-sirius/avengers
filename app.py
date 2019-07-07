from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sys import stdout

def log(str):
	print(str, file=stdout)

app = Flask(
	__name__,
	template_folder="frontend/templates",
	static_folder="frontend/static",)

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




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)