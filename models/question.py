#!/usr/bin/python
""" holds class Question"""
#import models
from models.base_model import BaseModel
from os import getenv
from models import Base
from flask_sqlalchemy import SQLAlchemy

# import sqlalchemy
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
#from web_dynamic.app import Base

class Question(BaseModel, Base):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Questions'

    id_survey_section = Column(Integer, ForeignKey('Survey_Sections.id'))
    id_survey = name = Column(String(128), nullable=False)
    name_question = Column(String(255), nullable=False)
    description = Column(String(255))
    answer_required = Column(Integer, nullable=False)
    calculated = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)
    questions = relationship("Question_Option", backref="Questions")
