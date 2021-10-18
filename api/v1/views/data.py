#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, render_template, request

@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
def data():
    if request.method == "POST":
        data = request.form
        documentID = data['dni', 'pasaporte', 'extranjeria']
        name = data['name']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']
        """ cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbquestionario(nome, Departamento, dataResposta, quantidadeRealizada,quantidadeReal, valorProvisionado, valorUtilizado, ResultadoFinal, Observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, Departamento, dataResposta, quantidadeRealizada,quantidadeReal, valorProvisionado, valorUtilizado, ResultadoFinal, Observacao))
        mysql.connection.commit()
        cur.close() """
        return render_template('index.html')