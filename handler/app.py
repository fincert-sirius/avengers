from flask import Flask, request
from threading import Thread
from queue import Queue
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
        # magic...
        time.sleep(15)
        verdict = 0
        f = open('verdicts.json', mode='r')
        data = json.load(f)
        data[domain] = verdict
        f.close()
        f = open('verdicts.json', mode='w')
        json.dump(data, f)
        f.close()
            

#----------------------------------------

logging.basicConfig(level='INFO')

# read config
config = None
with open('config.yml', mode='r') as f:
    config = yaml.safe_load(f)
    logging.info("Config loaded")

app = Flask(__name__)

domainsQueue = Queue()

handlingThread = Thread(target=handling, args=(domainsQueue, ))
handlingThread.start()

#-----------------------------------------

@app.route('/handle')
def api():
    domain = request.args.get('domain')
    domainsQueue.put(domain)
    return 'added to queue'1

@app.route('/results')
def results():
    with open('verdicts.json', mode='r') as f:
        data = json.load(f)
        return json.dumps(data)
    return 'error'
    


app.run(host=config['host'], port=config['port'])


