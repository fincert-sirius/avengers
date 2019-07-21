import requests
from src.page import Page, Chrome_page
import PyChromeDevTools
import time


class Page_getter:
	def get_page(self, url):
		pass


class Page_getter_requests(Page_getter):
	def get_page(self, url):
		html = requests.get(url).content

		return Page(
			url=url,
			html=html
		)


class Page_getter_chrome(Page_getter):
	def get_page(self, url):
		if not url.startswith('https://') and not url.startswith('http://'):
			url = 'https://' + url

		chrome = PyChromeDevTools.ChromeInterface(
			host="localhost",
			port=9222
		)
		chrome.Browser.setWindowBounds(
			windowId=1,
			bounds={
				'width': 1600,
				'height': 900
			}
		)

		chrome.Page.enable()
		chrome.Page.navigate(url=url)
		chrome.wait_event("Page.loadEventFired", timeout=60)
		time.sleep(10)
		# print(chrome.Page.getNavigationHistory())
		url = chrome.Page.getNavigationHistory()['result']['entries'][-1]['url']
		id = chrome.DOM.getDocument()['result']['root']['nodeId']
		return Chrome_page(
			chrome=chrome,
			url=url,
			html=chrome.DOM.getOuterHTML(nodeId=id)['result']['outerHTML']
		)


page_getter = Page_getter_chrome()
