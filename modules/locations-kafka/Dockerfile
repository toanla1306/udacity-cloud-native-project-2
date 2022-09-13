FROM python:3.7-alpine
RUN mkdir /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY ./modules/locations-kafka/requirements.txt requirements.txt
COPY ./modules/locations-kafka/app/location_kafka_consumer.py location_kafka_consumer.py

COPY ./modules/locations-kafka/app/database database/
COPY ./modules/locations-kafka/app/models.py models.py
COPY ./modules/locations-kafka/app/schemas.py schemas.py
COPY ./modules/locations-kafka/app/services.py services.py

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "python", "location_kafka_consumer.py" ]