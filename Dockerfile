FROM python:3.9.2-slim-buster

WORKDIR /api
RUN apt-get update
RUN apt-get -y install git

COPY OPT-GENERAL-MODELS/ /api/

RUN pip install -r requirements.txt;

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
RUN sudo apt-get install git-lfs

WORKDIR /api/opt-2.7b

RUN git-lfs install
RUN git lfs pull --include="pytorch_model.bin"

WORKDIR /api

CMD ["python" , "./app.py"]




