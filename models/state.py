#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    ...
    if HBNB_TYPE_STORAGE != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]

