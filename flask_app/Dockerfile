FROM python:3.9.2-slim-buster

WORKDIR usr/src/flask_app

RUN apt-get update -y

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
