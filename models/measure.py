#!/usr/bin/python
""" holds class Question"""
import models
from models import Base
from models.base_model import BaseModel
# from models.survey_section import Survey_Section
# from models.question_option import Question_Option
from models.question import Question
from os import getenv

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

class Measure(BaseModel, Base):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Measures'

    id_question = Column(Integer, ForeignKey(Question.id))
    media = Column(Float, nullable=False)
    desv_std = Column(Float, nullable=False)
    score = Column(Float, nullable=False)
    # answer_options = relationship(Question_Option, backref="question")
