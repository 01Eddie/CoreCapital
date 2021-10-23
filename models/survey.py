#!/usr/bin/python3
"""This module defines a class Survey"""

from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from models import Base
from datetime import datetime
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship


class Survey(BaseModel, Base):
    """This class defines a survey by various attributes"""
    __tablename__ = 'Surveys'

    name_survey = Column(String(100), nullable=False)
    description = Column(String(255))
    nro_questions = Column(Integer, nullable=False)
    surveys = relationship("SurveySections", backref("survey"))

