# Avengers web resources handle standalone microservice

from flask import Flask, request
from threading import Thread
from queue import Queue
from handler import Handler
import logging
import json
import yaml
import time

#---------------------------------------

def handling(q):
    logging.info('Handler thread started')
    while True:
        domain = q.get()
        logging.info('Handling resource {}...'.format(domain))

        h = Handler()
        result = h.handle(domain)
        info = {}
        info['score'] = result[0]
        info['category'] = result[1]
        info['comment'] = result[2]
        info['time'] = int(time.time())

        f = open('verdicts.json', mode='r')
        data = json.load(f)
        data[domain] = info
        f.close()
        f = open('verdicts.json', mode='w')
        json.dump(data, f)
        f.close()

        logging.info('Handling was completed.')


#----------------------------------------

logging.basicConfig(level='INFO')

# read config
config = None
with open('config.yml', mode='r') as f:
    try:
        config = yaml.safe_load(f)
        logging.info("Config loaded")
    except:
        logging.fatal("Cannot load config")
        exit(0)

app = Flask(__name__)

domainsQueue = Queue()

handlingThread = Thread(target=handling, args=(domainsQueue, ))
handlingThread.start()

#-----------------------------------------

@app.route('/add')
def api():
    domain = request.args.get('domain')
    domainsQueue.put(domain)
    return 'added to queue'

@app.route('/results')
def results():
    try:
        f = open('verdicts.json', mode='r')
        data = json.load(f)
        f.close()
    except:
        data = {}
    f = open('verdicts.json', mode='w')
    json.dump({}, f)
    f.close()
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'])


