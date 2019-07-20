from enum import Enum
from handler.app import db

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
	score = db.Column(db.Text, default='0')
	screen = db.Column(db.Text)
	reg_mail = db.Column(db.Text)
	criterions = db.Column(db.Text, default='{}')
	date = db.Column(db.Text)
