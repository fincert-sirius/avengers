from base64 import b64decode
from bs4 import BeautifulSoup as Bs
class Page:
	def __init__(self, url, html):
		if not url.startswith('https://'):
			url = 'https://' + url

		self.url = url
		self.html = Bs(html, 'html.parser')

		url = url[8:]

		self.domain = url

	def get_url(self):
		return self.url

	def get_domain(self):
		return self.domain

	def get_html(self):
		return self.html
		
class Chrome_page(Page):
	def __init__(self, url, html, chrome):
		super().__init__(
			url = url,
			html = html
		)

		self.chrome = chrome

	def save_screenshot(self, file):
		data = self.chrome.Page.captureScreenshot()['result']['data']
		data = b64decode(data)
		with open(file, 'wb') as file:
			file.write(data)