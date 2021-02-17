#!/usr/bin/python3
"""
123654987321
"""


from models.base_model import BaseModel
import os
import json


class FileStorage:
    __file_path = "salmen.JSON"
    open(__file_path, 'a')
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        a = {}
        for key, value in self.__objects.items():
            a[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(a, f)

    def reload(self):
        idclasses = {'BaseModel': BaseModel}
        data = {}
        if(os.stat(self.__file_path).st_size is not 0):
            with open(self.__file_path) as f:
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = \
                        idclasses[value['__class__']](**value)
