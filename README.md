# Avengers Sirius

## Installation

### Docker

- ensure you have **docker** installed
- build docker image: `docker build -t avengers .`
- run docker container: `docker run --name avengers -p 5000:5000 avengers`

### Manually

- ensure you have **python3** and **npm** (for building frontend) installed
- make virtual env: `python3 -m venv env`
- activate virtual env: `source env/bin/activate`
- install packages for backend: `pip install -r requirements.txt`
- update your database: `FLASK_APP=app.py flask db upgrade`
- run flask app: `FLASK_APP=app.py flask run`

#Govno
1.
- sudo docker container run -d -p 9222:9222 zenika/alpine-chrome --no-sandbox --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222
2.
- export FLASK_APP=app.py
- flask run
3.
- export FLASK_APP=handler/app.py
- export FLASK_RUN_PORT=5001
- flask run