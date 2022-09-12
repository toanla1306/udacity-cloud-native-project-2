FROM python:3.7-alpine
RUN mkdir /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY requirements.txt requirements.txt
COPY app/location_kafka_consumer.py location_kafka_consumer.py

COPY app/database database/
COPY app/models.py models.py
COPY app/schemas.py schemas.py
COPY app/services.py services.py

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "python", "location_kafka_consumer.py" ]