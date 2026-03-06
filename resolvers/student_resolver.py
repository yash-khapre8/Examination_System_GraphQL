from database import db
from models.student import Student
from models.attempt import Attempt

class StudentResolver:
    @staticmethod
    def get_all_students():
        """Fetch all students from the database."""
        return Student.query.all()

    @staticmethod
    def get_student_by_id(student_id):
        """Fetch a single student by their primary key ID."""
        return Student.query.get(student_id)

    @staticmethod
    def create_student(name, email, status='active'):
        """Create a new student entry and commit to DB."""
        student = Student(name=name, email=email, status=status)
        db.session.add(student)
        db.session.commit()
        return student

    @staticmethod
    def update_student(student_id, name=None, email=None, status=None):
        student = Student.query.get(student_id)
        if not student:
            return None
        if name: student.name = name
        if email: student.email = email
        if status: student.status = status
        db.session.commit()
        return student

    @staticmethod
    def delete_student(student_id):
        student = Student.query.get(student_id)
        if not student:
            return False
        db.session.delete(student)
        db.session.commit()
        return True

    @staticmethod
    def get_attempts_by_student(student_id):
        return Attempt.query.filter_by(student_id=student_id).all()
