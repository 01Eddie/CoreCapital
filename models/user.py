#!/usr/bin/python
""" holds class User"""
# import models
from models.base_model import BaseModel
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from models import db
from datetime import datetime
# import sqlalchemy
#from sqlalchemy import Column, String, Integer
#from sqlalchemy.orm import relationship

class User(BaseModel, db.Model):
    __tablename__ = "Users"
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nro_document = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
#    active = db.Column(db.Integer, nullable=False)
#    deleted_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#    created_by = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#    updated_by = db.Column(db.Integer, nullable=True)
#    deleted_by = db.Column(db.Integer, nullable=True)
    id_type_document = db.Column(db.Integer, db.ForeignKey('Type_Document.id'))
 
# modelo
"""
* `id`      int NOT NULL AUTO_INCREMENT ,
 `id_type_doc`  int NOT NULL ,
 `name`         varchar(100) NOT NULL ,
 `lastname`     varchar(255) NOT NULL ,-
 `email`        varchar(100) NOT NULL ,
 `nro_document` varchar(25) NOT NULL ,----
 `password`     varchar(255) NOT NULL ,
 `phone`        varchar(20) NOT NULL ,
 `active`       tinyint(1) NOT NULL ,
* `created_at`   datetime NOT NULL ,
* `updated_at`   datetime NULL ,
 `deleted_at`   datetime NULL ,
 `created_by`   int NOT NULL ,------
 `updated_by`   int NULL ,
 `deleted_by`   int NULL ,

"""
