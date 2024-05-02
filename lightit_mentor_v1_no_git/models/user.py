'''
User module
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
import models

class User(BaseModel, Base):
    ''' users table'''
    if models.storage_t == "db":
        __tablename__ = 'users'
        name = Column(String(100))
        father_name = Column(String(100))
        grand_father_name = Column(String(100))
        email = Column(String(100))
        phone_number = Column(String(14))
        password = Column(String(100))
        user_type = Column(Enum('Parent', 'student'))
    else: 
        name = ""
        father_name = ""
        grand_father_name = ""
        user_type = ""
        email = ""
        phone_number = ""
        password = ""
    
    # def __init__(self, *args, **kwargs):
    #     """initializes Place"""
    #     super().__init__(*args, **kwargs)

    # if models.storage_t != "db":
    #     @property
    #     def student(self):
    #         """getter for list of student instances related to the user"""
    #         student_list = []
    #         all_students = models.storage.all(Student)
    #         for student in all_students.values():
    #             if student.user_id == self.id:
    #                 student_list.append(student)
    #         return student_list
