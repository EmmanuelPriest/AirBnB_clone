#!/usr/bin/python3

'''Defines the class City'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class City that inheritted class BaseModel

        Attributes:
            state_id (str): The state identification
            name (str): The name of the city

    '''

    state_id = ""
    name = ""
