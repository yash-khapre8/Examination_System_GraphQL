from database import db
from models.exam import Exam
from models.question import Question
from models.option import Option
from models.attempt import Attempt
from models.response import Response
from datetime import datetime

class ExamResolver:
    @staticmethod
    def get_all_exams():
        """Retrieve all available exams."""
        return Exam.query.all()

    @staticmethod
    def get_exam_by_id(exam_id):
        """Retrieve a specific exam by ID."""
        return Exam.query.get(exam_id)

    @staticmethod
    def create_exam(title, duration, status='upcoming'):
        """Initialize a new exam container."""
        exam = Exam(title=title, duration=duration, status=status)
        db.session.add(exam)
        db.session.commit()
        return exam

    @staticmethod
    def start_exam(student_id, exam_id):
        """
        Starts an exam for a student.
        - Prevents multiple attempts.
        - Validates exam status (must be 'ongoing').
        """
        # Check if exam is ongoing
        exam = Exam.query.get(exam_id)
        if not exam or exam.status != 'ongoing':
            return None # Or raise an error in a real app
        
        # Check for existing attempts
        existing_attempt = Attempt.query.filter_by(student_id=student_id, exam_id=exam_id).first()
        if existing_attempt:
            return None # Already attempted or started
        
        attempt = Attempt(student_id=student_id, exam_id=exam_id, status='started')
        db.session.add(attempt)
        db.session.commit()
        return attempt

    @staticmethod
    def submit_exam(student_id, exam_id, answers):
        """
        Calculates the score based on provided answers and saves them as Responses.
        - Validates that an attempt was started.
        - Marks attempt as 'submitted'.
        """
        attempt = Attempt.query.filter_by(student_id=student_id, exam_id=exam_id, status='started').first()
        if not attempt:
            return None
        
        exam = Exam.query.get(exam_id)
        if not exam:
            return None
        
        total_marks = 0
        obtained_marks = 0
        
        for q in exam.questions:
            total_marks += q.marks
            # Find student's answer for this question
            student_answer = next((a for a in answers if int(a['question_id']) == q.id), None)
            
            selected_option_id = student_answer['option_id'] if student_answer else None
            
            # Record response
            resp = Response(attempt_id=attempt.id, question_id=q.id, selected_option_id=selected_option_id)
            db.session.add(resp)
            
            if selected_option_id:
                option = Option.query.get(selected_option_id)
                if option and option.question_id == q.id and option.is_correct:
                    obtained_marks += q.marks
        
        score = (obtained_marks / total_marks * 100) if total_marks > 0 else 0
        
        attempt.score = score
        attempt.status = 'submitted'
        db.session.commit()
        return attempt
