from enum import Enum
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))


class SiteStatus(Enum):
    NEW = 0
    PROCESSING = 1
    BLOCKED = 2
    GOOD_SITE = 3


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), unique=True)
    status = db.Column(db.Enum(SiteStatus), default=SiteStatus.PROCESSING)
    comment = db.Column(db.Text)
    whois_data = db.Column(db.Text)
    score = db.Column(db.Text)
    screen = db.Column(db.Text)
