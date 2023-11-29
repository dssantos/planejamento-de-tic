# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN pip install -r requirements.txt
COPY . /code/