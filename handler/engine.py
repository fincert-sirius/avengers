import time
import socket
import yaml
from ipwhois import IPWhois
from app import db
from models import Site, SiteStatus

def handle(domain):
    time.sleep(15) # magic

    verdict = 0
    comment = 'Some notes'
    category = 'lokhotron'

    whois = get_whois('domain')
    if whois == 'error':
        print('This web-site does not exists.')
        return

    site = Site(url=domain, comment=comment, whois_data=whois, status=SiteStatus.NEW)
    db.session.add(site)
    db.session.commit()

def get_whois(domain):
    ip = get_ip(domain)
    if ip == 'error':
        return 'error'
    obj = IPWhois(ip)
    info = obj.lookup_whois()
    return info

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return 'error'
