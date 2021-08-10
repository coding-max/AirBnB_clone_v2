#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv


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
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("Review", backref="place")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """returns the list of Reviews"""
            reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if self.id == review.place_id:
                    reviews.append(review)
            return reviews
