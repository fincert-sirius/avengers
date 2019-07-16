import time
import socket
import yaml
import whois
import json
from app import db
from models import Site, SiteStatus

def handle(domain):
    time.sleep(15) # magic

    verdict = 0
    comment = 'Some notes'
    category = 'lokhotron'

    site = Site.query.filter(Site.url == domain).one_or_none()

    whois = get_whois(domain)
    if whois == 'error':
        print('This web-site does not exists.')
        db.session.delete(Site.id)
        db.session.commit()
        return
    site.whois_data = json.dumps(whois, ensure_ascii=False, separators=(',',':'))
    site.status = SiteStatus.NEW

    db.session.add(site)
    db.session.commit()

def get_whois(domain):
    try:
        return whois.whois(domain)
    except:
        return 'error'