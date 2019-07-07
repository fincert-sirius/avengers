from src import rules

# All rules that will be checked
default_rules = [Susp_ending(), Susp_words(), Keywords(), Check_minus(), Many_subdomains()]

class Scorer:
	def __init__(self, rules):
		self.rules = rules

	def get_score(self, domain):
		for rule in self.rules:
			score += rule.get_score(domain)

		return score

default_scorer = Scorer(rules = default_rules)