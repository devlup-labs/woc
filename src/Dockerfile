FROM python:3.10-buster

RUN pip install pipenv

RUN mkdir -p /app

COPY . /app
COPY Pipfile  /app/
COPY Pipfile.lock /app/

WORKDIR /app

RUN pipenv install --system --deploy
