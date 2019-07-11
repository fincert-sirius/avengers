import requests
from src.page import Page
from selenium import webdriver

class Page_getter:
	def get_page(self, url):
		pass

class Page_getter_requests(Page_getter):
	def get_page(self, url):
		html = requests.get(url).content
		
		return Page(
			url = url,
			html = html
		)

class Page_getter_selenium(Page_getter):
	def get_page(self, url):
		driver = webdriver.Chrome()
		driver.get(url)
		html = driver.page_source
		driver.close()
		return html

page_getter = Page_getter_requests()