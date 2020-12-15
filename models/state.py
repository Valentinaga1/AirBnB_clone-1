#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """ Getter attribute cities that returns the list of
        City instances with state_id equals to the current State.id"""
        lst = []
        cities = storage.all(City).values()

        for city in cities:
            if self.id == city.state_id:
                lst.append(city)

        return lst
