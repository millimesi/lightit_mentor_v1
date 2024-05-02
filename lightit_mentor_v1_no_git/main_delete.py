#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.mentor import Mentor
from models.student import Student
from models.mentor_request import MentorRequest
from models.engine.file_storage import FileStorage

fs = FileStorage()

# All States
all_user = fs.all()
# all_user = fs.all(User)
print("All States: {}".format(len(all_user.keys())))
for state_key in all_user.keys():
    print(all_user[state_key])

# new_user = User()
# new_user.name = "California"
# fs.new(new_user)
# fs.save()
# all_user = fs.all(User)

# print("All States: {}".format(len(all_user.keys())))
# for state_key in all_user.keys():
#     print(all_user[state_key])

# fs.delete(new_user)

# all_user = fs.all(User)
# print("All States: {}".format(len(all_user.keys())))
# for state_key in all_user.keys():
#     print(all_user[state_key])