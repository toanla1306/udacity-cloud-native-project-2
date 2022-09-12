from kafka import KafkaConsumer
import json
from services import LocationService

TOPIC_NAME = 'test-topic'
# KAFKA_SERVER = 'localhost:9092'
KAFKA_SERVER = 'kafka.default.svc.cluster.local'
GROUP_ID = 'console-consumer-53977'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER, group_id=GROUP_ID)
for message in consumer:
    location_message = message.value.decode('utf-8')
    location_message_json = json.loads(location_message)
    LocationService.create(location_message_json)