#!/usr/bin/python
""" holds class Type_document"""
import models
from models.base_model import BaseModel
from os import getenv
from models import db
# import sqlalchemy
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship

class TypeDocument(BaseModel, db.Module):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
