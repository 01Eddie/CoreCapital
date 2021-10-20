#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request

@app_views.route('/questions', strict_slashes=False)
def quiz():
    return render_template('questions.html')
