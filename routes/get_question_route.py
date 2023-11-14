from flask import jsonify
from constants import HTTP_GOOD_RESULT
from models import *
from app import db, app, respond_with_error


@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = db.session.query(Question).get(id)
    if question is not None:
        return jsonify({'text': question.text,
                        'answers': [answer.text for answer in question.answers]
                        }), HTTP_GOOD_RESULT
    else:
        return respond_with_error("There's no question which correspond to the given id.")

