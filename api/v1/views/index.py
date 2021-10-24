#!/usr/bin/python3
""" Index """

from flask import jsonify

# from models import storage

from models.question import Question
from models.data import Data
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """

    classes = [Data, Question]
    names = ["data", "question"]

    num_objs = {}
    # for i in range(len(classes)):
        # num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
