#!/usr/bin/python3
""" objects that handle all default RestFul API  for answers"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
from models.question import Question
from models import session
from models.survey_section import Survey_Section

@app_views.route('/answers', methods=['POST'], strict_slashes=False)
def save_answers():
    """
    Return all answers
    """
    # print(request.get_json())
    # print('despues de request')
    # print(request.data)



#     all_questions = session.query(Question).all()
#     list_question = []
#     for question in all_questions:
#         questionOpt = question.to_dict()
#         # if not question.answer_options:
#         #     print(question.name_question)
#         questionOpt["answer_options"] = [op.to_dict() for op in question.answer_options] if question.answer_options else []
#         section = session.query(Survey_Section).filter_by(id=question.id_survey_section).first()
#         questionOpt["section_name"] = section.name_section if section is not None else ''
#         # print(question.answer_options)
#         list_question.append(questionOpt)
    return jsonify({'status': 'ok'})
