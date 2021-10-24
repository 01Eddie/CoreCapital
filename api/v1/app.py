#!/usr/bin/python3

from flask import abort, jsonify, make_response, render_template, request, Flask, flash, redirect, url_for

# from models.engine.db_storage import DBStorage
# from web_dynamic import app

# from models import storage
# from flask import Flask, app, render_template, make_response, jsonify
from flask_cors import CORS
from os import getenv
from os import environ
from api.v1.views import app_views
# from models import db

app = Flask(__name__)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

cors = CORS(app, resource={r"/api/v1/*": {"origins": "*"}})

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/prueba_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/prueba')
def prueba():
    return "hello"

# @app.teardown_appcontext
# def close_db(error):
#     """ Close Storage """
#     storage.close()


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
    # db.init_app(app)
    # host = environ.get('HBNB_API_HOST') # Host del mysql
    # port = environ.get('HBNB_API_PORT') # Port del mysql
    # if not host:
    #     host = '0.0.0.0'
    # if not port:
    #     port = '5001'
    app.run(host='0.0.0.0', port='5001', threaded=True)
