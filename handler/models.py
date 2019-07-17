from app import db
from enum import Enum

class SiteStatus(Enum):
    NEW = 0
    PROCESSING = 1
    BLOCKED = 2
    GOOD_SITE = 3

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    status = db.Column(db.Enum(SiteStatus), default=SiteStatus.PROCESSING)
    comment = db.Column(db.Text)
    whois_data = db.Column(db.Text)

