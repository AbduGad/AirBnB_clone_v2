#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):# "Create State name = California"
        """Instatntiates a new model"""
        if not kwargs or 'id' not in kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
            print(type(self.created_at), '1111111111')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        print(type(self.created_at), '************')
        print(type(self))
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
