#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates the database storage to create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))

        if getenv("HBNB_ENV ") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dic_of_objects = {}
        if cls and cls in classes.values():
            all_objetcs = self.__session.query(cls).all()
            for obj in all_objetcs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                value = obj
                dic_of_objects[key] = value
        elif cls is None:
            # acá guarda clase por clase todas sus filas en caso tal de que
            # la clase No esté vacía.
            for cls in classes.values():
                all_objetcs = self.__session.query(cls).all()
                for obj in all_objetcs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    value = obj
                    dic_of_objects[key] = value
        return dic_of_objects

    def new(self, obj):
        """Method to add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Method to commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method delete from the current database session obj if not None"""
        # obj = cls.id, dentro de una clae, sería una fila de esa clase
        if obj:
            self.__session.delete((obj))

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
