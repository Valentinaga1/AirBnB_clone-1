#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""

            objects = models.storage.all(City)
            list_of_city = []
            for city in objects.values():
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city
