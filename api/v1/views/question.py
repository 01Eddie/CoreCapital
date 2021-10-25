#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
from models.question import Question

@app_views.route('/questions', method=['GET'], strict_slashes=False)
def quiz():
    """
    Return all questions
    """
    list_question = []
    all_questions = Question.query.all()
    for question in all_questions:
        list_question.append(question.to_dict())
    return jsonify(list_question)
