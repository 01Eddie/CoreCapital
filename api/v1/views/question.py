#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
from models.question import Question
from models import session


@app_views.route('/questions', methods=['GET'], strict_slashes=False)
def all_question():
    """
    Return all questions
    """
    all_questions = session.query(Question).all()
    list_question = []
    for question in all_questions:
        list_question.append(question.to_dict())
    return jsonify(list_question)


@app_views.route('/surveys/<survey_id>/sections/<section_id>/questions/<questions_order>', methods=['GET'], strict_slashes=False)
def question(survey_id, section_id, questions_order):
    """
    Return all questions
    """
    # surveys = session.query(Question).filter(Question.id_survey==1)
    surveys = session.query(Question).filter(Question.id_survey==survey_id).filter(Question.id_survey_section==section_id).filter(Question.order==questions_order).first()
    if surveys is None:
        return jsonify( {"error": "Not found"}), 404
    print(surveys)
    return jsonify(surveys.to_dict())
