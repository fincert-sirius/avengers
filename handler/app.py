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
import engine

logging.basicConfig(level='INFO')

config = {}
with open('config.yml', mode='r') as f:
    try:
        config = yaml.safe_load(f)
        logging.info("Config loaded")
    except:
        logging.fatal("Cannot load config")
        exit(0)

def handling_process(q):
    logging.info('Handler thread started')
    while True:
        domain = q.get()
        logging.info('Handling resource {}...'.format(domain))
        engine.handle(domain)
        logging.info('Handling was completed.')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}:{}/{}".format(
    config['db_user'], config['db_pwd'], config['db_host'], config['db_port'], config['db_name'])
db = SQLAlchemy(app)

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
