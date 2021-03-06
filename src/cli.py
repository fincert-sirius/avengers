from app import app
import click
from src.rules import domain
from src import scorer, page_getter

@app.cli.command('check')
@click.argument('domain')
def check_domain(domain):
	print(scorer.default_scorer.get_score(domain))

@app.cli.command('get_html')
@click.argument('domain')
def get_html(domain):
	print(page_getter.page_getter.get_page(domain))
