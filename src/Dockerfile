FROM python:3.8-alpine

ARG BUILD_DEPS="gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libjpeg libffi-dev openjdk8"
RUN apk --no-cache add ${BUILD_DEPS}
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile* ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --dev \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' \+

WORKDIR /app
COPY . /app