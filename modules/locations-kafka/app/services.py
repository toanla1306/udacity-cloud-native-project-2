import logging
from datetime import datetime, timedelta
from typing import Dict, List

from database import session
from models import Location
from schemas import LocationSchema

from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logging.basicConfig(filename="log.txt", level=logging.DEBUG)


class LocationService:
    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        session.add(new_location)
        session.commit()

        return new_location
