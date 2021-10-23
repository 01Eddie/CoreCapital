#!/usr/bin/python
""" This module defines a class Question_Option"""

#import models
from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from models import db
#import sqlalchemy
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship


class Question_Option(BaseModel, db.Model):
    """This class defines a question_option by various attributes"""
    __tablename__ = 'Question_Options'

    id_question = db.Column(db.Integer, db.ForeignKey('Question.id'))
    id_survey = db.Column(db.Integer, nullable=False)
    id_survey_section = db.Column(db.Integer, nullable=False)
    name_option = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Integer)
    order = db.Column(db.Integer, nullable=False)
    answers = db.relationship("Answer", cascade="all", backref="Question_Options")
