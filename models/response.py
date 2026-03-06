from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Response(db.Model):
    __tablename__ = 'responses'

    id: Mapped[int] = mapped_column(primary_key=True)
    attempt_id: Mapped[int] = mapped_column(ForeignKey('attempts.id'), nullable=False)
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    selected_option_id: Mapped[int] = mapped_column(ForeignKey('options.id'), nullable=True)

    attempt = relationship("Attempt", back_populates="responses")
    question = relationship("Question")
    selected_option = relationship("Option")

    def __repr__(self):
        return f'<Response attempt:{self.attempt_id} question:{self.question_id}>'
