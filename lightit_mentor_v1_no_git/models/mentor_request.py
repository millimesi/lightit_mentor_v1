'''
User module
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship
import models


class MentorRequest(BaseModel, Base):
    '''Mentor request Class'''
    if models.storage_t == "db":
        __tablename__ = 'Mentor requests'
        student_id = Column(
            String(60), ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
        mentor_id = Column(
            String(60), ForeignKey('mentors.id', ondelete='CASCADE'), nullable=False)
        request_status = Column(Enum('Pending', 'Accepted', 'Rejected'))
        student = relationship(
            "Student", backref="mentor_requests", cascade="all, delete, delete-orphan", single_parent=True)
        mentor = relationship(
            "Mentor", backref="mentor_requests", cascade="all,delete, delete-orphan", single_parent=True)
    else:
        student_id = ""
        mentor_id = ""
        request_status = "pending"

    # def __init__(self, *args, **kwargs):
    #     """initializes city"""
    #     super().__init__(*args, **kwargs)
