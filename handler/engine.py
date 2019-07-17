import time
import socket
import yaml
import whois
import json
import logging
from app import db
from models import Site, SiteStatus

logging.basicConfig(level="INFO")

def handle(domain):
    time.sleep(15) # magic

    verdict = 0
    comment = 'Some notes'
    category = 'lokhotron'

    site = Site.query.filter(Site.url == domain).one_or_none()

    if site == None:
        logging.error("This url should be already in database")

    w = whois.query(domain)
    w['creation_date'] = str(w['creation_date'])
    w['expiration_date'] = str(w['expiration_date'])
    print(w)

    site.whois_data = json.dumps(w, sort_keys=True)
    site.status = SiteStatus.NEW

    db.session.add(site)
    db.session.commit()
