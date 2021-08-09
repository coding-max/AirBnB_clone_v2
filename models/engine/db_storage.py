#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from os import getenv

from sqlalchemy.sql.schema import MetaData
from models.base_model import Base

class DBStorage():
    """new engine, sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv(HBNB_MYSQL_USER),
                                              getenv(HBNB_MYSQL_PWD),
                                              getenv(HBNB_MYSQL_HOST),
                                              getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        if getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True) # puede ser que le pase mal los parametros

    def all(self, cls=None): #revisar esto despues porque lo hizo el maxi
        """queries on the current database session"""
        objects = {}
        for class in classes.value:
            if class is cls or cls is None:
                for element in self.__session.query(class).all():
                    objects[element.__class__.__name__+"."+element.id] = element
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        