#!/usr/bin/python
""" holds class Type_document"""
#import models
from models.base_model import BaseModel
from os import getenv
from models import Base
from flask_sqlalchemy import SQLAlchemy

# import sqlalchemy
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship

class Type_Document(BaseModel, Base):
    __tablename__ = "Type_Document"

#    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(45), nullable=False)
    type_documents = relationship("User", backref("Type_Document"))
