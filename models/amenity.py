#!/usr/bin/python3

'''Defines class Amenity'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class Amenity that inherits class BaseModel

        Attribute:
            name (str): The name of amenity in the state/city

    '''

    name = ""
