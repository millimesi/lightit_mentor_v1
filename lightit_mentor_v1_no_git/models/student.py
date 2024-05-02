'''
User module
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship
import models

class Student(BaseModel, Base):
    '''Student class'''
    if models.storage_t == "db":
        __tablename__ = 'students'
        name = Column(String(100), nullable=False)
        father_name = Column(String(100), nullable=False)
        grand_father_name = Column(String(100), nullable=False)
        grade_level = Column(Integer)
        phone_number = Column(String(14), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
        user = relationship(
            "User", backref="student", cascade="all, delete, delete-orphan", single_parent=True)
    else:
        name = ""
        father_name = ""
        grand_father_name = ""
        grade_level = 0
        phone_number = ""
        user_id = ""
    
    # def __init__(self, *args, **kwargs):
    #     """initializes Place"""
    #     super().__init__(*args, **kwargs)
