#!/usr/bin/python3
from os import getenv

"""
Create a unique FileStorage instance for your application.
A variable storage, an instance of FileStorage
"""
storage_t = getenv('STORAGE')
if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()