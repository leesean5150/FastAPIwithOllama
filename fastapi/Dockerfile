FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

CMD fastapi run --reload