from bs4 import BeautifulSoup as Bs
from tld import get_tld
class Page:
	def __init__(self, url, html):
		self.url = url
		self.html = Bs(html, 'html.parser')

	def get_url(self):
		return self.url

	def get_domain(self):
		domain = self.url
		if domain.startswith('*.'):
			domain = domain[2:]
	
		try:
			res = get_tld(domain, as_object=True, fail_silently=True, fix_protocol=True)
			domain = '.'.join([res.subdomain, res.domain])
		except Exception:
			pass

		return domain

	def get_html(self):
		return self.html
		