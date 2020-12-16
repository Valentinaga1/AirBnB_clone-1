#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
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
            # me traigo todos los objetos del objects de storage que son
            # ciudades
            objects = models.storage.all(City)
            list_of_city = []
            for city in objects.values():
                # esto me va a devolver {class.id = {state_id:"parametros"},
                # {state_ide:"parametross"}}. cuando llamamos all nos está
                # retornando una lista de objetos, aún sin serializar, no es
                # diccionario, accedemos a los objetos a través de un punto
                if city.state_id == self.id:
                    # si el state_id == al current id que es self.id
                    list_of_city.append(city)
            return list_of_city
