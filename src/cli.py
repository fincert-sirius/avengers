from app import app
import click
from src.rules import domain

@app.cli.command("rules")
def get_all_rules():
	rules = dict()
	for key, value in domain.__dict__.items():
		if key.startswith('__') or key.startswith('_'):
			continue

		rules[key] = value

	for key, value in rules.items():
		print('{} = {}'.format(key, value))