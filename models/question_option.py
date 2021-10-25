#!/usr/bin/python
""" This module defines a class Question_Option"""

#import models
from models import Base
from models.base_model import BaseModel
from models.question import Question
from flask_sqlalchemy import SQLAlchemy
# from models.answer import Answer
#import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Question_Option(BaseModel, Base):
    """This class defines a question_option by various attributes"""
    __tablename__ = 'Question_Options'

    id_question = Column(Integer, ForeignKey(Question.id))
    id_survey = Column(Integer, nullable=False)
    id_survey_section = Column(Integer, nullable=False)
    name_option = Column(String(200), nullable=False)
    value = Column(Integer)
    order = Column(Integer, nullable=False)
    # answers = relationship("Answer", cascade="all", backref="Question_Option")
