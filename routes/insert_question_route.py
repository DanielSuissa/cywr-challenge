from flask import request, jsonify
from constants import POLL_TYPE, TRIVIA_TYPE, HTTP_OBJECT_CREATED
from models import *
from validation import validate_fields, validate_field
from app import db, app, respond_with_error


@app.route('/api/v1/questions', methods=['POST'])
def insert_question():
    data = request.get_json()
    if validate_fields(data, [('text', str), ('type', str), ('answers', list)]):
        question = Question(text=data['text'], type=data['type'])
        db.session.add(question)
        db.session.commit()

        question_type = data['type']
        answer_list = data['answers']
        # insert answers to database
        for answer_str in answer_list:
            answer = Answer(question_id=question.id, text=answer_str, votes=0)
            db.session.add(answer)

        # for a trivia question mark the correct answer
        if question_type == POLL_TYPE:
            pass
        elif question_type == TRIVIA_TYPE:
            if validate_field(data, 'correctanswer', int):
                right_answer = Trivia(question_id=question.id, correct_answer=answer_list[data["correctanswer"]])
                db.session.add(right_answer)
            else:
                respond_with_error("A trivia question must have a correct answer indicated by an index of type int.")

        db.session.commit()
        return jsonify({'id': question.id}), HTTP_OBJECT_CREATED
    else:
        return respond_with_error('Missing Fields Or Unexpected Types.')
