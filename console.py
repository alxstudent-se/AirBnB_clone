#!/usr/bin/python3

import cmd
import re

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review

CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]
