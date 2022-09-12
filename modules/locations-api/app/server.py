import time
import json

from concurrent import futures
from kafka import KafkaProducer

import grpc
import locations_pb2
import locations_pb2_grpc

from google.protobuf.json_format import MessageToDict, MessageToJson

import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

from services import LocationService

class LocationServiceServer(locations_pb2_grpc.LocationServiceServicer):
    def GetLocationId(self, request, context):
        location_id = request.location_id
        response = LocationService.retrieve(location_id)
        if response:
            return locations_pb2.LocationResponseId(
                person_id = response.person_id,
                id = response.id,
                latitude = response.latitude,
                longitude = response.longitude,
                creation_time = response.creation_time
            )
        else:
            logging.debug("Cannot get any location with id %s....", location_id)

    def LocationCreate(self, request, context):
        print("Received a message!!")

        request_value = {
            "person_id": request.person_id, 
            "creation_time": request.creation_time,
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        print(request_value)

        TOPIC_NAME = 'locations'
        # KAFKA_SERVER = 'localhost:9092'
        KAFKA_SERVER = 'kafka.default.svc.cluster.local'
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        logging.debug("Kafka producer connected server....")
        kafka_data = json.dumps(request_value).encode()
        producer.send(TOPIC_NAME, kafka_data)
        producer.flush()
        logging.debug("Kafka producer sent message successfully....")

        return locations_pb2.LocationMessage(**request_value)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServiceServer(), server)

logging.debug("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop()