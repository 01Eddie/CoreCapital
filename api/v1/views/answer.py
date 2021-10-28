#!/usr/bin/python3
""" objects that handle all default RestFul API  for answers"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
from models.question import Question
from models import session
from models.survey_section import Survey_Section
from models.answer import Answer
from models.evaluation import Evaluation
from models.risk_profile import Risk_Profile
from models.user import User


@app_views.route('/risk_profile', methods=['POST'], strict_slashes=False)
def save_answers():
    """
    Return all answers
    """
    data = session.query(User).join(Evaluation, Evaluacion.id_user==User.id).join(Risk_Profile, Evaluation.id_risk_profile==Risk_Profile.id).first()
    if data is None: return abort
    print(data)
    # return jsonify({'status': 'ok'})
    return data



@app_views.route('/answers', methods=['POST'], strict_slashes=False)
def save_answers():
    """
    Return all answers
    """
    data = request.get_json()
    answer_list = data.get('answers')
    result = data.get('res')
    id_survey = data.get('id_survey')
    id_user = data.get('id_user')
    id_risk_profile = data.get('id_risk_profile')
    # print('despues de result')
    for answer in answer_list:
        ans = Answer(
        id_user = answer.get('user_id'),
        id_question_option = answer.get('id_question_option'),
        answer_value = answer.get('answer_value'),
        active = answer.get('active'),
        id_question = answer.get('id_question'),
        id_survey = answer.get('id_survey'),
        id_survey_section = answer.get('id_survey_section'),
        create_by = answer.get('user_id')
        )
        session.add(ans)

    evaluation = Evaluation(
        id_risk_profile = id_risk_profile,
        id_survey = id_survey,
        id_user = id_user,
        result = result
    )
    print(result)
    session.add(evaluation)

    session.commit()
    return jsonify({'status': 'ok'})
