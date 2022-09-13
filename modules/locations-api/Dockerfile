FROM python:3.8

RUN mkdir /app

WORKDIR /app

# RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY ./modules/locations-api/requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./modules/locations-api/app/locations.proto locations.proto
COPY ./modules/locations-api/app/server.py server.py

COPY ./modules/locations-api/app/database database/
COPY ./modules/locations-api/app/models.py models.py
COPY ./modules/locations-api/app/schemas.py schemas.py
COPY ./modules/locations-api/app/services.py services.py

RUN python -m grpc_tools.protoc -I./  --python_out=./ --grpc_python_out=./ locations.proto

EXPOSE 5005

ENTRYPOINT ["python", "server.py"]