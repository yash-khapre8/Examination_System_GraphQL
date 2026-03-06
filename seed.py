from app import create_app
from database import db
from models import Student, Exam, Question, Option
from datetime import datetime

def seed_data():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create a Student
        student = Student(name="Alice Johnson", email="alice@example.com")
        db.session.add(student)

        # Create an Exam
        exam = Exam(
            title="Python Fundamentals", 
            duration=45, 
            status="ongoing",
            date=datetime.utcnow()
        )
        db.session.add(exam)
        db.session.flush() # Get exam ID

        # Create a Question
        q1 = Question(exam_id=exam.id, text="What is the output of print(2**3)?", marks=5)
        db.session.add(q1)
        db.session.flush()

        # Create Options
        o1 = Option(question_id=q1.id, text="6", is_correct=False)
        o2 = Option(question_id=q1.id, text="8", is_correct=True)
        o3 = Option(question_id=q1.id, text="9", is_correct=False)
        db.session.add_all([o1, o2, o3])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
