from database import db
from models.question import Question
from models.option import Option

class QuestionResolver:
    @staticmethod
    def get_questions_by_exam(exam_id):
        return Question.query.filter_by(exam_id=exam_id).all()

    @staticmethod
    def create_question(exam_id, text, marks):
        question = Question(exam_id=exam_id, text=text, marks=marks)
        db.session.add(question)
        db.session.commit()
        return question

    @staticmethod
    def create_option(question_id, text, is_correct):
        option = Option(question_id=question_id, text=text, is_correct=is_correct)
        db.session.add(option)
        db.session.commit()
        return option
