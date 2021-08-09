#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="states")
    else:
        @property
        def cities(self):
            cities_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if self.id == city.state_id:
                    cities_list.append(city)
