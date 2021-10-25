#!/usr/bin/python
""" holds class Question"""
import models
from models import Base
# from models.question_option import Question_Option
from models.base_model import BaseModel
from models.survey_section import Survey_Section
from os import getenv

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Question(BaseModel, Base):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Questions'

    id_survey_section = Column(Integer, ForeignKey(Survey_Section.id))
    id_survey = Column(String(128), nullable=False)
    name_question = Column(String(255), nullable=False)
    description = Column(String(255))
    answer_required = Column(Integer, nullable=False)
    calculated = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)
    # questions = relationship("Question_Option", backref="Question")
