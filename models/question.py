from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Question(db.Model):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey('exams.id'), nullable=False)
    text: Mapped[str] = mapped_column(db.Text, nullable=False)
    marks: Mapped[int] = mapped_column(db.Integer, default=1)

    exam = relationship("Exam", back_populates="questions")
    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Question {self.id}>'
