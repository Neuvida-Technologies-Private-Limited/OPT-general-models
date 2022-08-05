FROM nvidia/cuda:11.7.0-runtime-ubuntu20.04

WORKDIR usr/src/flask_app

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get install unzip
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
LABEL com.nvidia.volumes.needed="nvidia_driver"

EXPOSE 8000

CMD ["gunicorn","-w","3","-b","0.0.0.0:8000","-t","360","wsgi:app"]
