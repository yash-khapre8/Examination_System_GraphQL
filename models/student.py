from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Student(db.Model):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    email: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(db.String(20), default='active')

    attempts = relationship("Attempt", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Student {self.name}>'
