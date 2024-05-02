'''
DB_storage Module
'''
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.mentor import Mentor
from models.student import Student
from models.mentor_request import MentorRequest
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Mentor": Mentor, "Student": Student,
           "MentorRequest": MentorRequest, "User": User}

class DBStorage:
    ''' DBStorage class'''
    __engine = None
    __session = None

    def __init__(self):
        ''' init method'''
        USER = 'mentors_dev'
        PWD = 'Million1234!'
        HOST = 'localhost'
        DB = 'light_it_mentors_db'
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PWD, HOST, DB), pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
        
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    