FROM nvidia/cuda:11.7.0-runtime-ubuntu20.04

WORKDIR usr/src/flask_app

RUN apt-get update -y

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
