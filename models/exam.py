from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Exam(db.Model):
    __tablename__ = 'exams'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(200), nullable=False)
    date: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow)
    duration: Mapped[int] = mapped_column(db.Integer)  # duration in minutes
    status: Mapped[str] = mapped_column(db.String(20), default='upcoming')  # upcoming, ongoing, completed

    questions = relationship("Question", back_populates="exam", cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="exam", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Exam {self.title}>'
