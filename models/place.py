#!/usr/bin/python3

'''Defines class Place'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''class Place that inheritted from class BaseModel

        Attributes:
            city_id (str): The City identification
            user_id (str): The User identification
            name (str): The name of the place
            description (str): Description of the place
            number_rooms (int): The number of rooms in the place
            number_bathrooms (int): The number of bathrooms in the place
            max_guest (int): The maximum number of guests for the place
            price_by_night (int): The price per night in the place
            latitude (float): The latitude of the place
            longitude (float): The longitude of the place
            amenity_ids (list): List of amenities in the place

    '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
