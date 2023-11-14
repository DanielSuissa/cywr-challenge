from flask import request, jsonify

from constants import TRIVIA_TYPE
from models import *
from validation import validate_field
from app import db, app, respond_with_error


@app.route('/api/v1/questions/<int:id>/vote', methods=['POST'])
def vote(id):
    data = request.get_json()
    if not validate_field(data, 'answer', str):
        respond_with_error("suggested answer must be of type string.")

    voted_answer_text = data['answer']
    possible_answers = db.session.query(Answer).filter_by(question_id=id)
    answer = possible_answers.filter_by(text=voted_answer_text).first()
    if answer is not None:
        result_json = {}
        # vote for correct answer
        answer.votes = answer.votes + 1
        db.session.commit()

        # retrieve votes for question
        all_votes = {}
        for ans in possible_answers:
            all_votes[ans.text] = ans.votes

        result_json["votes"] = all_votes

        # if this is a trivia question, add a remark on whether the user has voted right
        related_question = db.session.query(Question).get(id)
        if related_question is not None and related_question.type == TRIVIA_TYPE:
            # indicate whether this is the correct answer
            correct_answer_record = db.session.query(Trivia).filter_by(question_id=id).first()
            is_voted_correct = (answer.text == correct_answer_record.correct_answer)
            result_json["correct"] = is_voted_correct
        return jsonify(result_json)
    else:
        return respond_with_error("You have voted for an non-optional answer.")
