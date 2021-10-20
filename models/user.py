#!/usr/bin/python
""" holds class User"""
# import models
from models.base_model import BaseModel
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from models import db
# import sqlalchemy
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship

class User(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
