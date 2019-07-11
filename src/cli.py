from app import app
import click
from src.rules import domain
from src import scorer

@app.cli.command('check')
@click.argument('domain')
def check_domain(domain):
	print(scorer.default_scorer.get_score(domain))