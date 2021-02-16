#!/usr/bin/python3
"""
321321
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__[__class__] = self.__class__.__name__
        self.__dict__["created_at"] = \
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["updated_at"] = \
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (self.__dict__)
