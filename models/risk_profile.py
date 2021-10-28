#!/usr/bin/python
""" holds class Question"""
import models
from models import Base
from models.base_model import BaseModel
from os import getenv

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

class Risk_Profile(BaseModel, Base):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Risk_Profiles'

    name = Column(String(45), nullable=False)
    operator = Column(String(4), nullable=False)
    value = Column(Float, nullable=False)
