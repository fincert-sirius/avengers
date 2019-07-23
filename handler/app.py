from flask import Flask, request
from threading import Thread
from queue import Queue

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import logging
import json
import yaml
import time
import os

config = {}
with open('handler/config.yml', mode='r') as f:
	try:
		config = yaml.safe_load(f)
		logging.info("Config loaded")
	except:
		logging.fatal("Cannot load config")
		exit(0)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}:{}/{}".format(
	config['db_user'], config['db_pwd'], config['db_host'],
	config['db_port'], config['db_name'])
db = SQLAlchemy(app)


import handler.engine as engine
import handler.cli

logging.basicConfig(level='INFO')


def handling_process(q):
	logging.info('Handler thread started')
	while True:
		domain = q.get()
		logging.info('Handling resource {}...'.format(domain))
		engine.handle(domain)
		logging.info('Handling was completed.')

domainsQueue = Queue()
handlingThread = Thread(target=handling_process, args=(domainsQueue, ))
handlingThread.start()

@app.route('/add', methods=['POST'])
def api():
	domain = request.data.decode('utf-8')
	logging.info('Received domain: {}'.format(domain))
	domainsQueue.put(domain)
	return 'ok'

if __name__ == "__main__":
	
	app.run(host=config['host'], port=config['port'], debug=True)

