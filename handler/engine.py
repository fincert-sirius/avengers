import yaml
import json
import logging
from handler.app import db
from handler.models import Site, SiteStatus
from src.scorer import default_scorer as scorer
from src.page_getter import page_getter
from sys import stdout


logging.basicConfig(level="INFO")

def handle(domain):
	result = scorer.get_score(domain)
	res_dict = result.get_dict()

	page = page_getter.get_page(domain)
	site = Site.query.filter(Site.url == domain).one_or_none()

	if site is None:
		site = Site(url=domain)
		db.session.add(site)
		db.session.commit()

	page.save_screenshot('site_screens/{}.png'.format(site.id))

	w = result.get_whois()
	# print("1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", domain, site.screen, site.score, site.whois_data, sep='\n', file=stdout)
	if w is not None:
		w['creation_date'] = str(w['creation_date'])
		w['expiration_date'] = str(w['expiration_date'])

		for key in w.keys():
			w[key] = str(w[key])


	site.criterions = json.dumps(res_dict)
	site.screen = 'site_screens/{}.png'.format(site.id)
	site.score = str(result.get_sum())
	site.status = SiteStatus.NEW
	if w is not None:
		site.whois_data = json.dumps(w)
	else:
		site.whois_data = json.dumps({})

	print('>>>>>>>>>>>>', result, file=stdout)
	try:
		db.session.add(site)
		db.session.commit()
	except Exception as e:
		print(e, file=stdout)
