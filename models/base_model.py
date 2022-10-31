#!/usr/bin/python3

'''Defines the class BaseModel'''
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    '''Defines the Parent class of the AirBnB_clone project'''

    def __init__(self, *args, **kwargs):
        '''Initializes the BaseModel

        Args:
            *args (any): Not used
            **kwargs (dict): Key/value pairs of attributes
        '''
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''Prints string representation of the BaseModel instances in

        this format: [<class name>] (<self.id>) <self.__dict__>
        '''
        temp = self.__class__.__name__
        return "[{}] ({}) {}".format(temp, self.id, self.__dict__)

    def save(self):
        '''Update updated_at with the current time'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__

        of the instance
        '''
        return_dict = self.__dict__.copy()
        return_dict["__class__"] = self.__class__.__name__
        return_dict["created_at"] = return_dict["created_at"].isoformat()
        return_dict["updated_at"] = return_dict["updated_at"].isoformat()
        return return_dict
