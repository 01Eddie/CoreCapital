#!/usr/bin/python3

# from models import storage
from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for
from os import environ
# from flask_mysqldb import MySQL
from datetime import datetime
import models
from models import app
# from models import db
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from flask_cors import CORS

time = "%Y-%m-%dT%H:%M:%S.%f"

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/prueba_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usr_survey'
app.config['MYSQL_PASSWORD'] = 'survey_pwd'
app.config['MYSQL_DB'] = 'cp_survey_db'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# mysql = MySQL(app)
# db = SQLAlchemy(app)
# mysql = SQLAlchemy(appa)

# settings
app.secret_key = "mysecretkey"


""" cors = CORS(app, resource={r"/api/v1/*": {"origins": "*"}}) """

# @app.teardown_appcontext
# def close_db(error):
#     """ Close Storage """
#     storage.close()

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
        nmro_document = data['nmro_document']
        numero_documento = data['numero_documento']
        name = data['name']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']

        active="1"
        created_at = datetime.utcnow()
        created_by = '0'
        """ INSERT INTO `Users` (`id_user`,`id_type_doc`,`name`,`lastname`,`email`,`nro_document`,`phone`,`active`,`created_at`,`created_by`)
VALUES (1,1,'admin','admin','admin@gmail.com','11111111','999999999',1,'2021-10-18 02:17:06',1) """
        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO Type_Document (id_type_doc, nro_document, active) VALUES (%s,%s,%s)", (numero_documento, nmro_document, active))
        # cur.execute("INSERT INTO Users (id_type_doc, name, lastname, email, nro_document, phone, active, created_at, created_by) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (numero_documento, name, lastname, email, nmro_document, phone, active, created_at, created_by))
        # mysql.connection.commit()
        # flash('Added inversors successfully')
        user = User(name = "Jose")
        # db.session.add(user)
        # db.session.commit()
        print(User.id)
        return redirect(url_for('modal'))


@app.route("/modal", methods=['GET', 'POST'], strict_slashes=False)
def modal():
    return render_template('modal.html')

# @app.route("/modal", methods=['GET', 'POST'], strict_slashes=False)
# def modal():
#     return redirect(url_for('question'))


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
    db.create_all()
    print("despues de create_all")
    app.run(host='0.0.0.0', port='5000', threaded=True)
