FROM python:3.10

WORKDIR /opt/app
ENV DJANGO_SETTINGS_MODULE='config.settings'

RUN groupadd -r web && useradd -r -g web web

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi.ini uwsgi.ini

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
EXPOSE 8000

USER web
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]