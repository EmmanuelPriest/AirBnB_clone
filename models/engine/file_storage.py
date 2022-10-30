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
        obj_dict = FileStorage.__objects
        obj_dicton = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicton, f)

    def reload(self):
        '''Deserializes the JSON file __file_path to __objects,if it exists'''
        try:
            with open(FileStorage.__file_path) as f:
                dicton_obj = json.load(f)
                for n in dicton_obj.values():
                    class_name = n["__class__"]
                    del n["__class__"]
                    self.new(eval(class_name)(**n))
        except FileNotFoundError:
            return
