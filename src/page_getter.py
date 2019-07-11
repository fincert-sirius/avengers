import requests
from src.page import Page

class Page_getter:
	def get_page(self, url):
		pass

class Page_getter_requests(Page_getter):
	def get_page(self, url):
		html = requests.get(url)
		
		return Page(
			url = url,
			html = html
		)

page_getter = Page_getter_requests()
