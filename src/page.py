from bs4 import BeautifulSoup as Bs
class Page:
	def __init__(self, url, html):
		self.url = url
		self.html = Bs(html, 'html.parser')

	def get_url(self):
		return self.url

	def get_domain(self):
		return self.url

	def get_html(self):
		return self.html
		