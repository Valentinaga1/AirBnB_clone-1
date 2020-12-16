#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                             'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                             'amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            objects = models.storage.all(Review)
            list_of_review = []
            for review in objects.values():
                if review.state_id == self.id:
                    list_of_review.append(review)
            return list_of_review

        @property
        def amenities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            objects = models.storage.all(Amenity)
            list_of_amenity = []
            for ameni in objects.values():
                if ameni.place_id == self.id:
                    list_of_amenity.append(ameni)
            return list_of_amenity

        @amenities.setter
        def amenities(self, obj=None):
            if obj and obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
