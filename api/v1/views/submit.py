#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request
import models
from models.question import Question

@app_views.route('/submitq', methods=['POST', 'GET'])
def submitq():
    correctCount = 0
    """ Aqui deberia con esto deberia salir el agradecimiento al inversor, y enviar los datos que envio a la persona """
    for question in question_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correctOption = question.get_correct_opt()
        if selected_option == correctOption:
            correctCount = correctCount + 1