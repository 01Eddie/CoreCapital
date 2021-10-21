#!/usr/bin/python3
"""This module defines a class Survey"""

from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from models import db
from datetime import datetime
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship


class Survey(BaseModel, db.Model):
    """This class defines a survey by various attributes"""
    __tablename__ = 'Surveys'

    name_survey = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    nro_questions = db.Column(db.Integer, nullable=False)
    surveys = db.relationship("SurveySections", backref("survey"))

