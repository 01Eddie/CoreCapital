#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel
from os import getenv
# import sqlalchemy
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
from web_dynamic.app import db

class Question(BaseModel, db.Model):
    """ Aqui irá los modelos de datos """
    """ __tablename__ = '' """
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
