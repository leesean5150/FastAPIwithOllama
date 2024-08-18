FROM python:3.12.5-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

CMD fastapi run --reload