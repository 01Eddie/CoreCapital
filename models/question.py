#!/usr/bin/python
""" holds class Question"""
#import models
from models.base_model import BaseModel
from os import getenv
from models import db
from flask_sqlalchemy import SQLAlchemy

# import sqlalchemy
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
#from web_dynamic.app import db

class Question(BaseModel, db.Model):
    """ Aqui irá los modelos de datos """
    __tablename__ = 'Questions'

    id_survey_section = db.Column(db.Integer, db.ForeignKey('Survey_Sections.id'))
    id_survey = name = db.Column(db.String(128), nullable=False)
    name_question = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    answer_required = db.Column(db.Integer, nullable=False)
    calculated = db.Column(db.Integer, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    questions = db.relationship("Question_Option", backref("Questions"))
