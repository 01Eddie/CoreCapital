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
        questionOpt = question.to_dict()
        questionOpt["answer_options"] = [op.to_dict() for op in question.answer_options]
        # print(question.answer_options)
        list_question.append(questionOpt)
    return jsonify(list_question)


@app_views.route('/surveys/<survey_id>/sections/<section_id>/questions/<questions_order>', methods=['GET'], strict_slashes=False)
def question(survey_id, section_id, questions_order):
    """
    Return all questions
    """
    question = session.query(Question).filter(Question.id_survey==survey_id).filter(Question.id_survey_section==section_id).filter(Question.order==questions_order).first()
    if question is None:
        return jsonify( {"error": "Not found"}), 404
    print(question)
    questionOpt = question.to_dict()
    questionOpt["answer_options"] = [op.to_dict() for op in question.answer_options]
    return jsonify(questionOpt)

# @app_views.route('/surveys/<survey_id>/sections/<section_id>/questions/<questions_order>', methods=['POST'], strict_slashes=False)questionOpt
# """
# Save the questions answers
# """


