#!/usr/bin/python
""" holds class Amenity"""
import models
from models import Base
from models.base_model import BaseModel
from os import getenv
# import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.user import User
from models.question_option import Question_Option
from models.survey import Survey
from models.survey_section import Survey_Section
from models.question import Question

class Answer(BaseModel, Base):
    __tablename__ = 'Answer'
    id_user = Column(Integer, ForeignKey(User.id), nullable=False)
    id_question_option = Column(Integer, ForeignKey(Question_Option.id), nullable=False)
    answer_value = Column(Integer, nullable=True)
    active = Column(Boolean, default=False) # tinyint(1) NULL ,
    id_question = Column(Integer, ForeignKey(Question.id), nullable=False)
    id_survey = Column(Integer, ForeignKey(Survey.id), nullable=False)
    id_survey_section = Column(Integer, ForeignKey(Survey_Section.id), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow) # datetime NULL ,
    created_at = Column(DateTime, default=datetime.utcnow) # datetime NOT NULL ,
    deleted_at = Column(DateTime, default=datetime.utcnow) # datetime NULL ,
    create_by =  Column(Integer, nullable=False)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)


    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
