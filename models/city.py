#!/usr/bin/python3
""" Defines the City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city

    Attributes:
        name (str): name of city
        state_id (str): state which city is from
    """
    name = ""
    state_id = ""
