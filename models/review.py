#!/usr/bin/python3
""" Defines the Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review

    Attributes:
        text (str): review of place
        user_id (str): user who made review
        place_id (str): place that was reviewed
    """

    text = ""
    user_id = ""
    place_id = ""
