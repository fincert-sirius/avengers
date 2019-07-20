import time
import socket
import yaml
import whois
import json
import logging
from app import db
from models import Site, SiteStatus
from src.scorer import default_scorer as scorer
from src.page_getter import page_getter

logging.basicConfig(level="INFO")

def handle(domain):
    result = scorer.get_score(domain)
    res_dict = result.get_dict()

    page = page_getter.get_page(domain)
    site = Site.query.filter(Site.url == domain).one()

    page.save_screenshot('site_screens/{}.png'.format(site.id))

    #w = whois.query(domain)

    #w['creation_date'] = str(w['creation_date'])
    #w['expiration_date'] = str(w['expiration_date'])

    site.screen = f'site_screens/{site.id}.png'
    site.score = result.get_sum()
    #site.whois_data = json.dumps(w, sort_keys=True)
    site.status = SiteStatus.NEW

    db.session.add(site)
    db.session.commit()
