FROM nvidia/cuda:11.7.0-runtime-ubuntu20.04

WORKDIR usr/src/flask_app

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get install unzip
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
