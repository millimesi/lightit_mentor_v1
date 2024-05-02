'''
User module
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship
import models

class Mentor(BaseModel, Base):
    """ Mentor class"""
    if models.storage_t == "db":
        __tablename__ = 'mentors'
        name = Column(String(100), nullable=False)
        father_name = Column(String(100), nullable=False)
        grand_father_name = Column(String(100), nullable=False)
        Bio = Column(String(250), nullable=False)
        experience = Column(String(30))
        photo = Column(String(100), nullable=False)
        email = Column(String(100))
        phone_number = Column(String(14), nullable=False)
        password = Column(String(100), nullable=False)
    else:
        name = ""
        father_name = ""
        grand_father_name = ""
        Bio = ""
        experience = ""
        photo = ""
        email = ""
        phone_number = ""
        password = ""
    
    # def __init__(self, *args, **kwargs):
    #     """initializes Place"""
    #     super().__init__(*args, **kwargs)
