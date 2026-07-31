from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base

# Промежуточная таблица связывает студентов с курсами
student_courses = Table(
    "student_courses",
    Base.metadata,
    Column(
        "student_id",
        ForeignKey("students.id"),
        primary_key=True,
    ),
    Column(
        "course_id",
        ForeignKey("courses.id"),
        primary_key=True,
    ),
)


# ORM-модель таблицы студентов
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students",
    )


# ORM-модель таблицы курсов
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses",
    )
