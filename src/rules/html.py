import yaml

with open('config/suspicious.yaml', 'r') as f:
		suspicious = yaml.safe_load(f)

class Check_susp_title:
	def get_score(self, page):
		title = page.get_html().title.string

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
		pass_input = list(page.get_html().find_all('input', type='password'))
		if len(pass_input) == 0:
			return 0
		return 10

	def get_description(self):
		return """
			The page contains a password input.
		"""

class Check_hid_input:
	def get_score(self, page):
		attr = page.get_html().find_all('input', hidden='True')
		if len(attr) != 0:
			return 5

	def get_description(self):
		return """
			It just determines if the page contains a hidden form input.
		"""

class Check_multi_auth:
	def get_score(self, page):
		text = suspicious['multi-auth']
		html_text = page.get_html().get_text()
		col = 0
		for word in text:
			if word in html_text:
				col += 1

		if col >= 3:
			return 20

		return 0

	def get_description(self):
		return """
			It determines if the page is attempting to phish for
			multiple email services at once.
		"""
