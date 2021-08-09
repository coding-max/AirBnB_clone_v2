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

    def new(self, obj): #check afetr
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self): #check afetr
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None): #check afetr
        """delete from the current database session obj if not None"""
        if obj:
            for row in self.__session.query().all()
                self.__session.delete()
            self.save()

    def reload(self): #check afetr
        """"""