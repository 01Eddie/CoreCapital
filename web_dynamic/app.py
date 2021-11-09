#!/usr/bin/python3

# from models import storage
from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for, send_from_directory, current_app
from os import environ
from datetime import datetime
from api.v1.views import question
import models
from models import session
from models.question import Question
from models.user import User
from models.answer import Answer
from models.type_document import Type_Document
from models.survey_section import Survey_Section
from models.question_option import Question_Option
from models.survey import Survey
from models.evaluation import Evaluation
from models.risk_profile import Risk_Profile
# from models.question import Question
from flask_cors import CORS
from flask import session as flask_session
import pandas as pd
import smtplib
import os

time = "%Y-%m-%dT%H:%M:%S.%f"

app = Flask(__name__)


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usr_survey'
app.config['MYSQL_PASSWORD'] = 'survey_pwd'
app.config['MYSQL_DB'] = 'cp_survey_db'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# settings
app.secret_key = "mysecretkey"

""" cors = CORS(app, resource={r"/api/v1/*": {"origins": "*"}}) """

# @app.teardown_appcontext
# def close_db(error):
#     try:
#         print(error)
#         """ Close Storage """
#         session.close()
#     except:
#         raise

@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    r =  "<p>Hello, World!</p>"
    return render_template("index.html")

@app.route('/', methods=['POST'], strict_slashes=False)
def add_form():
    if request.method == 'POST':
        data = request.form
        """ numero_documento =[
            1: DNI
            2: Pasaporte
            3: Carnet de Extranjería]
        """
        user_Obj = session.query(User).filter(User.nro_document == data.get('nro_document')).first()
        # print(data)
        if user_Obj is not None:
            check_User = session.query(Answer).filter(Answer.id_user == user_Obj.id).first()
            if check_User is None:
                return redirect(url_for('modal'))
            return render_template('index.html')

        type_document = int(data['type_document'])
        nro_document = data['nro_document']
        name = data['name']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']

        active="1"
        created_at = datetime.utcnow()
        created_by = '0'
        """ INSERT INTO `Users` (`id_user`,`id_type_doc`,`name`,`lastname`,`email`,`nro_document`,`phone`,`active`,`created_at`,`created_by`)
VALUES (1,1,'admin','admin','admin@gmail.com','11111111','999999999',1,'2021-10-18 02:17:06',1) """
        user = User(
            name=name,
            lastname=lastname,
            email=email,
            id_type_document=type_document,
            nro_document=nro_document,
            phone=phone
            )
        session.add(user)
        session.commit()
        flask_session['user_id']=user.id
        return redirect(url_for('modal'))
        # return render_template('modal.html')




@app.route("/modal", methods=['GET', 'POST'], strict_slashes=False)
def modal():
    return render_template('modal.html')

# @app.route("/modal", methods=['GET', 'POST'], strict_slashes=False)
# def modal():
#     # return redirect(url_for('question'))
#     return redirect(url_for('modal.html'))

@app.route("/question", methods=['GET', 'POST'], strict_slashes=False)
def questions():
    # if request.method == 'POST':    
    # my_question = Question(question)
    # print("Questions")
    user_id = flask_session.get('user_id')
    return render_template('questions.html', user_id=user_id)



""" @app.route("/question", methods=['POST'])
def options_question():
    if request.method == 'POST':
        data = request.form
        print(data)
    return True """

@app.route("/final", methods=['GET', 'POST'], strict_slashes=False)
def final():
    msg = request.args.get("msg")
    if request.method == 'POST':
        user = session.query(User).filter(User.id == request.get_json().get('user_id')).first()
        user_id = request.get_json().get('user_id')
        print(user_id)
        email = "EMAIL HERE"
        # In the console PASSWORD=PASSWORD_HERE python3 -m web_dynamic.app
        message = "Subject: Tienes un usuario nuevo Usuario Numero: {}\n\nUna persona se acaba de registrar con el \n- Nombre: {}\n- Apellido: {}\n Email:{}\n- Telefono: {}".format(user.id, user.name, user.lastname, user.email, user.phone)
        # tolist = "Tienes un usuario nuevo Nmro: {}".format(user.id)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, os.getenv("PASSWORD"))
        # print("{}".format(os.getenv("PASSWORD")))
        server.sendmail(email, email, message)
        print("message enviado")
        return "Mensaje enviado", 200
    # else:
    return render_template('final.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        data = request.form
        # print(data)
        # flask_session['username']
        # username = data['username']
        # password = data['password']
        flask_session['username'] = data.get('username', '')
        flask_session['password'] = data.get('password', '')
        """ print(flask_session['username'])
        print(flask_session['password']) """
        if len(flask_session['username']) == 0 or len(flask_session['password']) == 0:
            return render_template('login.html')
        elif flask_session['username'] == "admin@corecapital.com" and flask_session['password'] == "corecapital2021":
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/dashboard', methods=['GET'], strict_slashes=False)
def dashboard():
    if 'username' in flask_session and 'password' in flask_session:
        # print('Loggedo como {}'.format(flask_session['username']))
        # answers = session.query(Answer, Type_Document, User, Question_Option, Question, Risk_Profile).join(User, User.id == Answer.id_user).join(Type_Document, Type_Document.id == User.id_type_document).join(Question_Option, Question_Option.id == Answer.id_question_option).join(Question, Question.id == Answer.id_question).join(Evaluation, User.id == Evaluation.id_user).join(Risk_Profile, Risk_Profile.id == Evaluation.id_risk_profile).all()

        answers = session.query(User, Type_Document, Evaluation, Risk_Profile).join(Type_Document, User.id_type_document == Type_Document.id).join(Evaluation, User.id == Evaluation.id_user).join(Risk_Profile, Risk_Profile.id == Evaluation.id_risk_profile).all()
        # answers = session.query(User, Type_Document, Evaluation, Risk_Profile).join(Type_Document, User.id_type_document == Type_Document.id).join(Evaluation, Evaluation.id_risk_profile == User.id).filter(Risk_Profile.id == User.id).all()
        # print(answers)
        """ names = pd.DataFrame(answers, columns=answers)
        ex = names.to_excel('dataCorePartners.xlsx') """
        
        return render_template('index-Admin.html', answers=answers)

@app.route('/dashboard-tables', methods=['GET'], strict_slashes=False)
def dashboard_tables():
    if 'username' in flask_session and 'password' in flask_session:
        # print('Loggedo como {}'.format(flask_session['username']))
        answers = session.query(User, Type_Document).join(Type_Document, User.id_type_document == Type_Document.id).all()
        # print(answers)
        return render_template('tables.html', answers=answers)

""" @app.route('/export', methods=['GET'], strict_slashes=False)
def export():
    return
 """
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    flask_session.pop('username', None)
    flask_session.pop('password', None)

    return redirect(url_for('login'))

@app.route('/download', methods=['GET', 'POST'])
def download():
    # df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
    #                "Patient ID": [123, 456],
    #                "Misc Data Point": [8, 53]})
    # df = pd.DataFrame([['a', 'b'], ['c', 'd']],
    # index=['row 1', 'row 2'],
    # columns=['col 1', 'col 2'])
    # df2 = df.to_excel("output.xlsx")

    # Create a Pandas dataframe from some data.
    data = [10, 20, 30, 40, 50, 60, 70, 80]
    questions = session.query(Question).all()
    users = session.query(User).all()
    answers = session.query(Answer, Type_Document, User, Question_Option, Question, Risk_Profile).join(User, User.id == Answer.id_user).join(Type_Document, Type_Document.id == User.id_type_document).join(Question_Option, Question_Option.id == Answer.id_question_option).join(Question, Question.id == Answer.id_question).join(Evaluation, User.id == Evaluation.id_user).join(Risk_Profile, Risk_Profile.id == Evaluation.id_risk_profile).all()

    # answers = session.query(Type_Document, User, Answer, Question_Option, Question).join(User, User.id_type_document == Type_Document.id).join(Answer, Answer.id_user == User.id).join(Question_Option, Question_Option.id == Answer.id_question_option).join(Question, Question.id == Answer.id_question).all()
    # answer_options = session.query(Answer, Question_Option).join(Answer, Answer.id_question_option == Question_Option.id).all()
    # print(questions)
    # list_n = []
    # if request.method == 'GET':
    #     for t, u, a, qo, q in answers:
    #         list_n.append([t.to_dict(), u.to_dict(), a.to_dict(), qo.to_dict(), qo.to_dict()])
        # return jsonify(list_n)

    answer_Doc = [t[1].name for t in answers]
    list_question = [q[4].name_question for q in answers]
    list_name = [un[2].name for un in answers]
    list_nmro_doc = [u[2].nro_document for u in answers]
    list_lastname = [ul[2].lastname for ul in answers]
    list_created = [cr[2].created_at for cr in answers]
    list_answered_question = [aq[3].name_option for aq in answers]
    list_question_size = [qs[0].answer_value for qs in answers]
    list_profile = [p[5].name for p in answers]
    
    df = pd.DataFrame({
        "Creado: ": list_created,
        "Nombre":list_name,
        "Apellido": list_lastname,
        "Documento": answer_Doc,
        "Numero de documento": list_nmro_doc,
        "Preguntas":list_question,
        "Respuesta contestada": list_answered_question,
        "Peso de la Pregunta": list_question_size,
        "Perfil de Riesgo": list_profile
        })

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter("CoreCapitalEvaluation.xlsx", engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object. Turn off the default
    # header and index and skip one row to allow us to insert a user defined
    # header.
    df.to_excel(writer, sheet_name='CoreCapital', startrow=1, header=False, index=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['CoreCapital']

    # Get the dimensions of the dataframe.
    (max_row, max_col) = df.shape

    # Create a list of column headers, to use in add_table().
    column_settings = []
    for header in df.columns:
        column_settings.append({'header': header})

    # Add the table.
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 12)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    # print("Archivo descargado!!")
    
    return send_from_directory(os.getcwd(), 'CoreCapitalEvaluation.xlsx')

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """ Main Function """
    # host = environ.get('HBNB_API_HOST') # Host del mysql
    # port = environ.get('HBNB_API_PORT') # Port del mysql
    # if not host:
    #     host = '0.0.0.0'
    # if not port:
    #     port = '5000'
    app.run(host='0.0.0.0', port='5000', threaded=True)
