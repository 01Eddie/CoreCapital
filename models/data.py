#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel
from os import getenv
from models import db
# import sqlalchemy
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship

class Data(BaseModel, db.Model):
    """ Aqui irá los modelos de datos del formulario
    name: a
    lastname: a
    dni, passport, etc: a
    correo: a
    telefono: a
        """
    """ __tablename__ = '' """
    name = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
