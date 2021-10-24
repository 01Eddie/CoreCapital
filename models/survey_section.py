#!/usr/bin/python3
"""This module defines a class Survey_Section"""
from models import Base
from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Survey_Section(BaseModel, Base):
    """This class defines a survey_section by various attributes"""
    __tablename__ = 'Survey_Sections'

    id_survey = Column(Integer, ForeignKey('surveys.id'))
    name_section = Column(String(100), nullable=False)
    description = Column(String(1024))
    questions = relationship("Question", cascade="all",
                             backref="Survey_Section")
