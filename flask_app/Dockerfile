FROM python:3.9.2-slim-buster

WORKDIR /usr/src/flask_app

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn","-w","2","--threads","2","-b","0.0.0.0:8000","-t","360","wsgi:app"]
