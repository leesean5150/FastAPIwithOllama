FROM python:3.10.0a7-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

CMD fastapi run --reload