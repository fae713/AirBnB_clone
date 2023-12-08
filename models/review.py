#!/usr/bin/python3
""" a class 'Review' that inherit BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Users review of place/house in the AirBnb app

    Attributes:
                place_id (str): The place id
                user_id (str): The user id
                text (str): The user review
    """

    place_id = ""
    user_id = ""
    text = ""
