# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORDKDIR /app

COPY requeriments.txt requeriments.txt
RUN pip3 install -r requeriments.txt

COPY . .
CMD [ "python3","main.py"]
