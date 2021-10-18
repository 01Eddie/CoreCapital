#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from models.engine.db_storage import DBStorage

storage_t = getenv("encuestaCP")
storage = DBStorage()
storage.reload()