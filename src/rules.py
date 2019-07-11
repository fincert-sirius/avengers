import yaml
import re
from tld import get_tld

# Temporary var for returning max score
const = 120

with open('config/suspicious.yaml', 'r') as f:
		suspicious = yaml.safe_load(f)

class Susp_ending:
	def get_score(self, domain):
		score = 0
		for t in suspicious['tlds']:
			if domain.endswith(t):
				score += 20
		return score

	def max_score(self):
		return const

	def get_description(self):
		return """
			Проверка на подозрительное окончание домена сайта. 
			(.cf, .tl, ...)
		"""


class High_entropy:
	def get_score(self, domain):
		return int(round(entropy.shannon_entropy(domain)*50))

	def max_score(self):
		return const

	def get_description(self):
		return """
			Рекомендуем не вдаваться в подробности. Честно, это очень трудно. 
		"""

class Susp_words:
	def get_score(self, domain):
		words_in_domain = re.split("\W+", domain)

		if words_in_domain[0] in ['com', 'net', 'org']:
			return 10
		return 0
	
	def max_score(self):
		return const

	def get_description(self):
		return """
			Проверка на наличие доменных окончаний не на своей позиции.
			(.com-info.net)
		"""

class Keywords:
	def get_score(self, domain):
		score = 0
		for word in suspicious['keywords']:
			if word in domain:
				score += suspicious['keywords'][word]
		return score

	def max_score(self):
		return const

	def get_description(self):
		return """
			Some keywords(...)
		"""


class Lev_dist:
	def get_score(self, domain):
		score = 0
		for key in [k for (k,s) in suspicious['keywords'].items() if s >= 70]:
			for word in [w for w in words_in_domain if w not in ['email', 'mail', 'cloud']]:
				if distance(str(word), str(key)) == 1:
					score += 70
		return score

	def max_score(self):
		return const

	def get_description(self):
		return """
			Подсчет расстояния Левенштейна для проверяемого 
			и предположительного доменов.
		"""


class Check_minus:
	def get_score(self, domain):
		if 'xn--' in domain:
			if domain.count('-') >= 6:
				return domain.count('-') * 3
		else:
			if domain.count('-') >= 4:
				return domain.count('-') * 3
		return 0

	def max_score(self):
		return const

	def get_description(self):
		return """
			Проверка на большое количество дефисов.
		"""

class Many_subdomains:
	def get_score(self, domain):
		if domain.count('.') >= 3:
			return domain.count('.') * 3
		return 0

	def max_score(self):
		return const

	def get_description(self):
		return """
			Большое количество субдоменов.
		"""