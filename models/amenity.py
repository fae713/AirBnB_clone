#!/usr/bin/python3
""" A class 'Amenity' that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents the armenities in the home

    Attributes:
            name (str): name of the amenity
    """
    name = ""
