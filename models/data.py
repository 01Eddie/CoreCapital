#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Data(BaseModel, Base):
    if models.storage_t == "db":
        """ Aqui irá los modelos de datos del formulario
        name: a
        lastname: a
        dni, passport, etc: a
        correo: a
        telefono: a
         """
        """ __tablename__ = '' """
        name = Column(String(128), nullable=False)
        lastname = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)