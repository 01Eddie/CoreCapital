#!/usr/bin/python3

# from models import storage
from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for
from os import environ
from datetime import datetime
from api.v1.views import question
import models
from models import session
from models.user import User
from models.answer import Answer
from models.type_document import Type_Document
# from models.question import Question
from flask_cors import CORS
from flask import session as flask_session

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
        print(data)
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
        """ else: """
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
def dashboard():
    if 'username' in flask_session or 'password' in flask_session:
        print('Loggedo como {}'.format(flask_session['username']))
        answers = session.query(Answer, User, Type_Document).join(User, User.id == Answer.id_user).join(Type_Document, User.id_type_document == Type_Document.id).all()
        print(answers)
        return render_template('index-Admin.html', answers=answers)

@app.route('/dashboard-tables', methods=['GET', 'POST'], strict_slashes=False)
def dashboard_tables():
    if 'username' in flask_session or 'password' in flask_session:
        print('Loggedo como {}'.format(flask_session['username']))
        answers = session.query(Answer, User, Type_Document).join(User, User.id == Answer.id_user).join(Type_Document, User.id_type_document == Type_Document.id).all()
        print(answers)
        return render_template('tables.html', answers=answers)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    flask_session.pop('username', None)
    return redirect(url_for('login'))


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
