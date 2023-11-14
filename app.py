import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from constants import *
from flask import jsonify
import os

# retrieve postgres credentials
db_credentials_uri = os.getenv(ENV_DB_CREDENTIALS_URI)
if db_credentials_uri is None:
    sys.exit("The required environment variables are not defined. Exiting program.")

# initialize Flask and configure a DB connection
app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = db_credentials_uri
db = SQLAlchemy(app)

# a utility function for returning an error
def respond_with_error(message):
    return jsonify({'error': message}), HTTP_SERVER_GENERAL_ERROR

# define route handlers
import routes.vote_route
import routes.get_question_route
import routes.insert_question_route


