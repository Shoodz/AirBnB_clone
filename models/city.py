#!/usr/bin/python3
"""The module below creates User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
