FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

ARG DEV=false

COPY requirements.txt /app/
COPY . /app/

WORKDIR /app
RUN pip install -r requirements.txt
