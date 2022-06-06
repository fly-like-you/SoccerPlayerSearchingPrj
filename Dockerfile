FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

COPY . /usr/src/app/

RUN apt-get install python-dev libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt