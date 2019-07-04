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