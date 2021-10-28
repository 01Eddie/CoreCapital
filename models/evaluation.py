#!/usr/bin/python
""" holds class Question"""
import models
from models import Base
from models.base_model import BaseModel
# from models.survey_section import Survey_Section
# from models.question_option import Question_Option
from models.question import Question
from models.survey import Survey
from models.user import User
from models.risk_profile import Risk_Profile
from os import getenv

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

class Evaluation(BaseModel, Base):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Evaluations'

    id_risk_profile = Column(Integer, ForeignKey(Risk_Profile.id))
    id_survey = Column(Integer, ForeignKey(Survey.id))
    id_user = Column(Integer, ForeignKey(User.id))
    result = Column(Float)
    # score = Column(Float, nullable=False)
