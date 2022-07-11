FROM python:3.9.2-slim-buster

WORKDIR /api

RUN apt-get update -y
RUN apt-get -y install git

COPY . /api/

RUN pip install -r requirements.txt;

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app"]

