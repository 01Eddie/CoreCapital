#!/usr/bin/python
""" holds class Type_document"""
#import models
from models.base_model import BaseModel
from os import getenv
from models import db
from flask_sqlalchemy import SQLAlchemy

# import sqlalchemy
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship

class Type_Document(BaseModel, db.Model):
    __tablename__ = "Type_Document"

#    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    type_documents = db.relationship("User", backref("Type_Document"))
