class Page:
	def __init__(self, url, html):
		self.url = url
		self.html = html

	def get_url(self):
		return self.url

	def get_domain(self):
		pass

	def get_html(self):
		return self.html
		