# Avengers Sirius

## Installation

- ensure you have **python3** and **npm** (for building frontend) installed
- make virtual env: `python3 -m venv env`
- activate virtual env: `source env/bin/activate`
- install packages for backend: `pip install -r requirements.txt`
- update your database: `FLASK_APP=app.py flask db upgrade`
- install packages for frontend: `npm i`
- build frontend: `./node_modules/.bin/webpack`
- run flask app: `FLASK_APP=app.py flask run`