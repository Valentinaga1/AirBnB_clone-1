#!/usr/bin/python3
""" New engine """
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


user = getenv('HBNB_MYSQL_USER')
psw = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
opt = getenv('HBNB_ENV')


class DBStorage():
    """ New engine DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, psw, host, db), pool_pre_ping=True)

        if opt == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ Query on the current database session
        """
        dic = {}

        classes = [State, City, User, Place, Review, Amenity]
        if cls in classes:
            sto = DBStorage.__session.query(cls)
            for row in sto:
                k = "{}.{}".format(row.__class__.__name__, row.id)
                dic[k] = row
        elif cls is None:
            for clas in classes:
                sto = DBStorage.__session.query(clas)
                for row in sto:
                    k = "{}.{}".format(row.__class__.__name__, row.id)
                    dic[k] = row
        return dic

    def new(self, obj):
        """ Add the object to the current database session
        """
        DBStorage.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session
        """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None
        """
        DBStorage.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
