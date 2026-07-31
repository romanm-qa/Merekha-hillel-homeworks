from database import Base, SessionLocal, engine
from models import Course, Student
from seed import create_courses, create_students


def add_student_to_course(session, student_name, course_title):
    course = (
        session.query(Course)
        .filter_by(title=course_title)
        .first()
    )

    if course is None:
        print(f'Курс "{course_title}" не найден.')
        return

    existing_student = (
        session.query(Student)
        .filter_by(name=student_name)
        .first()
    )

    if existing_student is not None:
        print(f'Студент "{student_name}" уже существует.')
        return

    student = Student(name=student_name)
    student.courses.append(course)

    session.add(student)
    session.commit()

    print(
        f'Студент "{student_name}" добавлен '
        f'на курс "{course_title}".'
    )


def show_students_by_course(session, course_title):
    course = (
        session.query(Course)
        .filter_by(title=course_title)
        .first()
    )

    if course is None:
        print(f'Курс "{course_title}" не найден.')
        return

    print(f'Студенты курса "{course_title}":')

    for student in course.students:
        print(f"- {student.name}")


def show_courses_by_student(session, student_name):
    student = (
        session.query(Student)
        .filter_by(name=student_name)
        .first()
    )

    if student is None:
        print(f'Студент "{student_name}" не найден.')
        return

    print(f'Курсы студента "{student_name}":')

    for course in student.courses:
        print(f"- {course.title}")


def update_student_name(session, current_name, new_name):
    student = (
        session.query(Student)
        .filter_by(name=current_name)
        .first()
    )

    if student is None:
        print(f'Студент "{current_name}" не найден.')
        return

    student.name = new_name
    session.commit()

    print(
        f'Имя студента изменено: '
        f'"{current_name}" → "{new_name}".'
    )


def delete_student(session, student_name):
    student = (
        session.query(Student)
        .filter_by(name=student_name)
        .first()
    )

    if student is None:
        print(f'Студент "{student_name}" не найден.')
        return

    session.delete(student)
    session.commit()

    print(f'Студент "{student_name}" удалён.')


if __name__ == "__main__":
    # Создаём в PostgreSQL все таблицы, описанные через Base
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        create_courses(session)
        create_students(session)
        add_student_to_course(session, "Roman Merekha", "Python")

        show_students_by_course(session, "Python")
        show_courses_by_student(session, "Roman Merekha")

        update_student_name(
            session,
            "Roman Merekha",
            "Roman Merekha Updated",
        )
        delete_student(session, "Colin Myers")

    print("Таблицы, курсы и студенты успешно созданы.")
