FROM python:3.7-alpine
LABEL maintainer MilanB

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers build-base postgresql-dev libpq-dev python3-dev musl-dev g++ unixodbc unixodbc-dev
RUN pip install psycopg2-binary
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user