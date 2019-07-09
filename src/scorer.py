from src.rules import domain
from src.rules import html
from collections import namedtuple

# All rules that will be checked
default_rules = [
	domain.Susp_ending(),
	domain.Susp_words(),
	domain.Keywords(),
	domain.Check_minus(),
	domain.Many_subdomains(),
	html.Check_susp_title(),
	html.Check_susp_text(),
	html.Check_2_auth(),
	html.Check_pass_input(),
	html.Check_multi_auth(),
	html.Check_hid_input()
]

Cause = namedtuple('Cause', ['rule', 'score'])

class Scorer:
	def __init__(self, rules):
		self.rules = rules

	def get_score(self, domain):
		result = Result()

		for rule in self.rules:
			score = rule.get_score(domain)
			if score != 0:
				result.add(rule, score)

		return result

class Result:
	def __init__(self, causes = []):
		self.causes = causes

	def add(self, rule, score):
		self.causes.append(
			Cause(rule, score)
		)

	def get_sum(self):
		score = 0
		for cause in self.causes:
			score += cause.score

		return score

	def get_causes(self):
		return self.causes

default_scorer = Scorer(rules = default_rules)