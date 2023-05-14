#!/usr/bin/python3
""" Defines the place class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a place

    Attributes:
        name (str): name of place
        user_id (str): user id in place
        city_id (str): city where place is in
        description (str): description of place
        number_bathrooms (int): number of bathrooms in place
        price_by_night (int): price of night's stay in place
        number_rooms (int): number of rooms in place
        longitude (float): longitudnal location of place
        latitude (float): latitudnal location of place
        max_guest (int): maximum number of guests allowed in place
        amenity_ids (list): list of amenities in place
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
