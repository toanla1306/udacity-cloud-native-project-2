import grpc
import locations_pb2
import locations_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = locations_pb2_grpc.LocationServiceStub(channel)
def request_location_id(stub):
    location_id = locations_pb2.LocationRequestId(location_id="30")

    response = stub.GetLocationId(location_id)

def create_location(stub):
    new_location = locations_pb2.LocationMessage(
        person_id="123",
        creation_time="2022-08-15 10:37:06.000000",
        latitude="55",
        longitude="66"
    )
    response = stub.LocationCreate(new_location)
    print(response)

create_location(stub)
