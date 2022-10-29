#!/usr/bin/python3

'''Defines class Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class Review that inherits class BaseModel

        Attributes:
            place_id (str): The Place identification under Review
            user_id (str): The user identification under Review
            text (str): The text to be Reviewed

    '''

    place_id = ""
    user_id = ""
    text = ""
