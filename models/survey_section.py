#!/usr/bin/python3
"""This module defines a class Survey_Section"""

from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from models import db
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship


class Survey_Section(BaseModel, db.Model):
    """This class defines a survey_section by various attributes"""
    __tablename__ = 'Survey_Sections'

    id_survey = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    name_section = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1024))
    questions = db.relationship("Question", cascade="all",
                             backref="Survey_Section")
