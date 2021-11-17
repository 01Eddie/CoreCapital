#!/usr/bin/python3
""" objects that handle all default RestFul API  for answers"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
from models.question import Question
import models
from models.survey_section import Survey_Section
from models.answer import Answer
from models.evaluation import Evaluation
from models.risk_profile import Risk_Profile
from models.user import User

# session = models.session

# @app_views.route('/risk_profile', methods=['POST'], strict_slashes=False)
# def save_answers():
#     """
#     Return all answers
#     """
#     data = session.query(User).join(Evaluation, Evaluacion.id_user==User.id).join(Risk_Profile, Evaluation.id_risk_profile==Risk_Profile.id).first()
#     if data is None: return abort
#     print(data)
#     # return jsonify({'status': 'ok'})
#     return data


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
    id_age = data.get('user_age')
    for answer in answer_list:
        ans = Answer(
        id_user=answer.get('user_id'),
        id_question_option=answer.get('id_question_option'),
        answer_value=answer.get('answer_value'),
        active=answer.get('active'),
        id_question=answer.get('id_question'),
        id_survey=answer.get('id_survey'),
        id_survey_section=answer.get('id_survey_section'),
        create_by=answer.get('user_id')
        )
        models.session.add(ans)
    models.session.commit()

    # Comparamos el id_risk_profile con el resultado obtenido
    if result is None:
        id_risk_profile = None;
        msg = 'Usted por el momento no puede acceder a nuestros productos.';
    elif result < -1:
        id_risk_profile = 1
        msg = 'Usted tiene un perfil tipo: <b>Adverso</b></br></br>Un asesor se comunicará con usted próximamente.'
    elif result <= 0:
        id_risk_profile = 2
        msg = 'Usted tiene un perfil tipo: <b>Moderado Adverso</b></br></br>Un asesor se comunicará con usted próximamente.'
    elif result > 0.75:
        id_risk_profile = 4
        msg = 'Usted tiene un perfil tipo: <b>Agresivo</b></br></br>Un asesor se comunicará con usted próximamente.'
    else:
        id_risk_profile = 3;
        msg = 'Usted tiene un perfil tipo: <b>Moderado Agresivo</b></br></br>Un asesor se comunicará con usted próximamente.'

    evaluation = Evaluation(
        id_risk_profile=id_risk_profile,
        id_survey=id_survey,
        id_user=id_user,
        result=result
    )
    models.session.add(evaluation)
    models.session.commit()

    print(evaluation)

    user = models.session.query(User).filter(User.id==id_user).first()
    user.age = id_age
    models.session.add(user)
    models.session.commit()

    print(result)
    print(user.age)

    print(models.session.query(Evaluation).all())
    return jsonify({'status': 'ok', 'msg': msg})
