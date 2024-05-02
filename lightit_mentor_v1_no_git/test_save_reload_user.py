#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.mentor import Mentor
from models.student import Student
from models.mentor_request import MentorRequest

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.name = "Betty"
my_user.father_name = "Meseret"
my_user.grand_father_name = "yirdaw"
my_user.email = "airbnb@mail.com"
my_user.user_type = "parent"
my_user.phone_number = "0911155060"
my_user.password = "root"
my_user.save()
print(my_user)
print('--------------------------')
mentor1 = Mentor()
mentor1.name = "mentor1"
mentor1.father_name = "mentor1 father"
mentor1.grand_father_name = "mentor1 grandfather "
mentor1.Bio = "i am very good"
mentor1.experience = "2 years"
mentor1.photo = "link"
mentor1.email = "link"
mentor1.phone_number = "number"
mentor1.password = "mentor1paSSWORD"
print(mentor1)
print('--------------------------')
student1 = Student()
student1.name = "student1"
student1.father_name = "student1f"
student1.grand_father_name = "student1g"
student1.grade_level = 4
student1.phone_number = ""
student1.user_id = my_user.id
print(student1)
print('--------------------------')
request1 = MentorRequest()
request1.student_id = student1.id
request1.mentor_id = mentor1.id
request1.request_status = "accepted"
print(request1)
print('--------------------------')
print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)