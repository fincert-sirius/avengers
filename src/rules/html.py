import yaml
from handler.handler import _Handler
from src.parser import parser

with open('config/suspicious.yaml', 'r') as f:
		suspicious = yaml.safe_load(f)

handl = _Handler()

class Check_susp_title:
	def get_score(self, page):
		title = page.get_html().title

		if (title == None):
			return 0

		title = title.string

		if title.lstrip() == '':
			return 0
		
		if title in suspicious['keywords']:
			return suspicious['keywords'][title]
		
		return 0

	def get_description(self):
		return """
			It determines if the page title contains any references
			to any brand's name.
		"""

class Check_susp_text:
	def get_score(self, page):
		text = suspicious['susp_text']
		html_text = page.get_html().get_text()

		if html_text == '':
			return 0

		html_text = parser(html_text)

		score = 0
		for word in text:
			if word in html_text:
				score += suspicious['susp_text'][word]

		return score

	def get_description(self):
		return """
			It determines if the page contains any common strings
			used in phishing pages.
		"""

class Check_2_auth:
	def get_score(self, page):
		text = suspicious['2FA']
		html_text = page.get_html().get_text()

		if html_text == '':
			return 0

		html_text = parser(html_text)

		score = 0
		for word in text:
			if word in html_text:
				score += suspicious['susp_text'][word]

		return score


	def get_description(self):
		return """
			The page may attempt to steal the two-factor authentication token.
		"""

class Check_pass_input:
	def get_score(self, page):
		soup = page.get_html()

		pass_input = soup.find_all('input', type='password')

		if len(pass_input) == 0:
			return 0

		return suspicious['pass_input']['input']

	def get_description(self):
		return """
			The page contains a password input.
		"""

class Check_hid_input:
	def get_score(self, page):
		attr = list(page.get_html().find_all('input', hidden='True'))
		if len(attr) != 0:
			return suspicious['pass_input']['hid_input']
		return 0

	def get_description(self):
		return """
			It just determines if the page contains a hidden form input.
		"""

class Check_multi_auth:
	def get_score(self, page):
		text = suspicious['multi-auth']
		html_text = page.get_html().get_text()

		if html_text == '':
			return 0

		html_text = parser(html_text)

		col = 0
		for word in text:
			if word in html_text:
				col += 1

		if col >= 3:
			return suspicious['multi-auth']['has_multi-auth']

		return 0

	def get_description(self):
		return """
			It determines if the page is attempting to phish for
			multiple email services at once.
		"""

class Check_time:
	def get_score(self, page):
		html_text = page.get_html().find_all('div')

		for word in html_text:
			if word == '\d{2}:\d{2}:\d{2}' or word == '\d{2}:\d{2}:\d{2}\n' or word == '\d{2}:\d{2}:\d{2},':
				return suspicious['check_time']['has_timer']

		return 0

	def get_description(self):
		return """
			It determines if the page has a time-date counter.
		"""

class Check_cloudflare:
	def get_score(self, page):
		domain = page.get_domain()
		whois = handl.get_whois(domain)
		words = list(whois['asn_description'].split(' '))

		if 'Cloudflare' in words or 'Cloudflare,' in words or 'Cloudflare\n' in words:
			return suspicious['DNS']['Cloudflare']
		return 0

	def get_description(self):
		return """
			It determines if domain is registered in Cloudflare.
		"""

# class Check_redirect:
# 	def get_score(self, page):


# 	def get_description(self):
# 		return """
# 			It determines if domain is redirected to another.
# 		"""