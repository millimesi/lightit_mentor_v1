'''
File storge module
'''


import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.mentor import Mentor
from models.student import Student
from models.mentor_request import MentorRequest

class FileStorage:
    ''' File storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''Return all objects of the class'''
        if cls:
            dict_of_cls = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    dict_of_cls[key] = value
            return dict_of_cls
        return FileStorage.__objects

    def new(self, obj):
        '''creates new object'''
        if obj:
            obj_key = f'{obj.__class__.__name__}.{obj.id}'
            FileStorage.__objects[obj_key] = obj

    def save(self):
        ''' saves the seralized __object '''
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as file:
            json.dump(new_dict, file)

    def reload(self):
        ''' saves the objects deserialized from file'''
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as file:
                new_dict = json.load(file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

    def delete(self, obj=None):
        ''' delete obj from __objects if it’s inside
        - if obj is equal to None, the method should not do anything
        '''
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                    del FileStorage.__objects[key]
                    self.save()

