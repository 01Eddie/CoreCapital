#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


"""
initialize the models package
"""
HBNB_MYSQL_USER='usr_survey'
HBNB_MYSQL_PWD='survey_pwd'
HBNB_MYSQL_HOST='localhost'
HBNB_MYSQL_DB='cp_survey_db'


Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
from models.user import User
from models.question import Question
from models.answer import Answer

Base.metadata.create_all(engine)
sess_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(sess_factory)
session = Session()

# from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for
# from os import getenv
# from models.engine.storage import DBStorage
# from flask_sqlalchemy import SQLAlchemy
# from web_dynamic import app

# storage_t = getenv("encuestaCP")
# storage = DBStorage()
# storage.reload()

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/prueba_
# otros
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'usr_survey'
# app.config['MYSQL_PASSWORD'] = 'survey_pwd'
# app.config['MYSQL_DB'] = 'cp_survey_
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# = SQLAlchemy(pp)

# storage
