#!/usr/bin/python3
""" a class 'Place' that inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place/house uploaded to the AirBnB app

    Attributes:
            city_id (str): The city id
            user_id (str): The user id
            name (str): The name of the place
            description (str): The description of the place
            number_rooms (int): Total room number
            number_bathrooms (int): Total bathroom number
            max_guest (int): Max guests allowed
            price_by_night (int): Cost of room a night
            latitude (float): Latitude of the place
            longitude (float): Longitude of the place
            amenity_ids (str): The list of amenities
        """

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
