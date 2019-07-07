from src import rules

# All rules that will be checked
default_rules = [
	rules.Susp_ending(),
	rules.Susp_words(),
	rules.Keywords(),
	rules.Check_minus(),
	rules.Many_subdomains(),
]

class Scorer:
	def __init__(self, rules):
		self.rules = rules

	def get_score(self, domain):
		result = []

		for rule in self.rules:
			score = rule.get_score(domain)
			if score != 0:
				result.append({
					'desc': rule.get_description(),
					'score': score	
				})

		return result

default_scorer = Scorer(rules = default_rules)