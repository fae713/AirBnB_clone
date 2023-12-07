#!/usr/bin/python3
""" A class 'City' that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ A city in the AirBnB app

    Attributes:
             state_id (str): The state the city is in.
             name (str): name of the city
    """
    state_id = ""
    name = ""
