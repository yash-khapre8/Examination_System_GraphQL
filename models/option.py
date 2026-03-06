from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Option(db.Model):
    __tablename__ = 'options'

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    text: Mapped[str] = mapped_column(db.String(200), nullable=False)
    is_correct: Mapped[bool] = mapped_column(db.Boolean, default=False)

    question = relationship("Question", back_populates="options")

    def __repr__(self):
        return f'<Option {self.id}>'
