import logging
from datetime import datetime, timedelta
from typing import Dict, List

from database import Session
from models import Location
from schemas import LocationSchema

from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

# session = Session()

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            Session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == int(location_id))
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location
        # with db.Session() as dbs:
        #     request_data = {"id": int(location_id)}
        #     location = db.s.first(Location, **request_data)
        #     db.s.flush()
        #     db.s.commit()
        #     return location
        #     dbs.close()