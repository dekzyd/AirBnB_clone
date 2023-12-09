#!/usr/bin/python3

import uuid
from models import storage
from datetime import datetime
'''defines all common attributes/methods for other classes'''


class BaseModel:
    '''creates a basemodel for other classes'''
    def __init__(self, *args, **kwargs):
        '''initializes a basemodel object'''

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        timefmt = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, timefmt))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        '''representation of the object as a string'''
        return "[{}] ({}) {}".format(
                type(self).__name__,
                self.id, self.__dict__
                    )

    def save(self):
        '''saves the object'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''shows all object attributes in dictionary format'''
        dictionary = self.__dict__
        dictionary['__class__'] = type(self).__name__
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        return dictionary
