from src.rules import domain
from src.rules import html
from collections import namedtuple
import inspect
from src import page_getter

Cause = namedtuple('Cause', ['rule', 'score'])

class Scorer:
	def __init__(self, rules=[]):
		self.rules = rules

	def get_score(self, domain):
		result = Result()
		page = page_getter.page_getter.get_page(domain)

		for rule in self.rules:
			score = rule.get_score(page) or 0
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

	def __str__(self):
		s = str(self.get_sum()) + '\n'
		for cause in self.causes:
			s += str(cause) + '\n'

		return s


class Autoload_scorer(Scorer):
	def __init__(self, *modules):
		super().__init__()
		for module in modules:
			for key, value in module.__dict__.items():
				if key.startswith('_') or key.startswith('__'):
					continue
				if inspect.isclass(value):
					self.rules.append(value())


default_scorer = Autoload_scorer(domain, html)