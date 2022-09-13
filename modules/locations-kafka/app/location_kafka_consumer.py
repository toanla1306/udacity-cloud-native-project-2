from kafka import KafkaConsumer
import json
from services import LocationService

TOPIC_NAME = 'locations'
# KAFKA_SERVER = 'localhost:9092'
KAFKA_SERVER = 'kafka.default.svc.cluster.local'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    location_message = message.value.decode('utf-8')
    location_message_json = json.loads(location_message)
    LocationService.create(location_message_json)