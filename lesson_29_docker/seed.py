import random

from faker import Faker

from models import Course, Student

# Генератор случайных тестовых данных
fake = Faker()


def create_courses(session):
    if session.query(Course).count() > 0:
        return

    courses = [
        Course(title="Python"),
        Course(title="SQL"),
        Course(title="Git"),
        Course(title="Docker"),
        Course(title="The Automation"),
    ]

    session.add_all(courses)
    session.commit()


def create_students(session):
    if session.query(Student).count() > 0:
        return

    courses = session.query(Course).all()
    students = []

    for _ in range(20):
        student = Student(name=fake.name())

        # Выбираем для студента от 1 до 3 случайных курсов
        student.courses = random.sample(
            courses,
            k=random.randint(1, 3),
        )

        students.append(student)

    session.add_all(students)
    session.commit()
