from src import rules

# All rules that will be checked
rules = [Susp_ending(), Susp_words(), Keywords(), Check_minus(), Many_subdomains()]

class scorer:
	def get_score(domain):
		for i in rules:
			score += i.get_score(domain)

		return score / len(rules)