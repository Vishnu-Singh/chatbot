# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /chatbot
COPY requirements.txt /chatbot/
RUN pip install -r requirements.txt
COPY . /chatbot/