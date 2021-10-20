#!/usr/bin/python3
"""
initialize the models package
"""


from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for
from os import getenv
# from models.engine.db_storage import DBStorage
from flask_sqlalchemy import SQLAlchemy
# from web_dynamic import app

# storage_t = getenv("encuestaCP")
# storage = DBStorage()
# storage.reload()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/prueba_db'
# otros
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usr_survey'
app.config['MYSQL_PASSWORD'] = 'survey_pwd'
app.config['MYSQL_DB'] = 'cp_survey_db'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)
