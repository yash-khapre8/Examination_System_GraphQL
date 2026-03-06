from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class Attempt(db.Model):
    __tablename__ = 'attempts'

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    exam_id: Mapped[int] = mapped_column(ForeignKey('exams.id'), nullable=False)
    score: Mapped[float] = mapped_column(db.Float, default=0.0)
    status: Mapped[str] = mapped_column(db.String(20), default='started')  # started, submitted
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="attempts")
    exam = relationship("Exam", back_populates="attempts")
    responses = relationship("Response", back_populates="attempt", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Attempt student:{self.student_id} exam:{self.exam_id} status:{self.status}>'
