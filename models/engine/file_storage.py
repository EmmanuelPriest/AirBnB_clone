#!/usr/bin/python3

'''Defines the FileStorage class'''
import json
import datetime
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Serializes instances to a JSON file and deserializes

    JSON file to instances
    Attributes:
        __file_path (str): The 'string path to the JSON file
        __objects (dict): Object dictionary instanstiated
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects obj with key <obj_class_name>.id'''
        file_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(file_name, obj.id)] = obj

    def save(self):
        '''Serializes __objects to the JSON file __file_path'''
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            objd = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(objd, f)

    def classes(self):
        '''Returns dict of valid classes and reference'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        '''Deserializes the JSON file __file_path to __objects,if it exists'''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[val["__class__"]](**val)
                        for key, val in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        '''Returns the valid attributes and their types for class_names'''
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
