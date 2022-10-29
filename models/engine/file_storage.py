#!/usr/bin/python3

'''Defines the FileStorage class'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''serializes instances to a JSON file and deserializes

    JSON file to instances
    Attributes:
        __file_path (str): The 'string path to the JSON file
        __objects (dict): Object dictionary instanstiated
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects obj with key <obj_class_name>.id'''
        key = (f"{obj.__class__.__name__}.{obj.id}")
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file __file_path'''
        obj_dictionary = {}

        for key, value in self.__objects.items():
            obj_dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding=utf-8) as f:
            json.dump(obj_dictionary, f)

    def reload(self):
        '''Deserializes the JSON file __file_path to __objects,if it exists'''
        try:
            with open(self.__file_path, "r", encoding=utf-8) as f:
                dictionary_obj = json.load(f)
                for key, value in dictionary_obj.items():
                    self.__objects[key] = eval(key.split(".")[0])(**value)
        except FileNotFoundError:
            return
