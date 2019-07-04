FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN flask db upgrade

ENV FLASK_APP app.py

EXPOSE 5000

CMD flask run --host=0.0.0.0
