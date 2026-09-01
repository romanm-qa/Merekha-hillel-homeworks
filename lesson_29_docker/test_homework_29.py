import pytest
from sqlalchemy import text

from database import Base, SessionLocal, engine
from homework_29 import (
    add_student_to_course,
    update_student_name,
    delete_student,
)
from models import Student, Course
from seed import create_courses


@pytest.fixture
def db_session():
    # Создаём таблицы, если их ещё нет
    Base.metadata.create_all(engine)

    session = SessionLocal()
    # Создаём курсы, необходимые для тестов
    create_courses(session)

    # Удаляем тестовые данные, оставшиеся после неудачного запуска
    test_students = (
        session.query(Student)
        .filter(Student.name.like("Docker Test%"))
        .all()
    )

    for student in test_students:
        session.delete(student)

    session.commit()

    yield session

    # Очищаем созданные тестами данные
    test_students = (
        session.query(Student)
        .filter(Student.name.like("Docker Test%"))
        .all()
    )

    for student in test_students:
        session.delete(student)

    session.commit()
    session.close()


def test_database_connection(db_session):
    """Проверяет, что соединение с базой данных работает."""
    # Выполняем простейший SQL-запрос напрямую через text(),
    # чтобы проверить, что соединение с базой реально работает
    result = db_session.execute(text("SELECT 1"))

    # .scalar() достаёт одно значение из результата запроса —
    # первую колонку первой строки
    assert result.scalar() == 1


def test_add_student_to_course(db_session):
    """Проверяет добавление студента и его привязку к курсу."""
    add_student_to_course(
        db_session,
        "Docker Test Student",
        "Python",
    )

    student = (
        db_session.query(Student)
        .filter_by(name="Docker Test Student")
        .first()
    )

    assert student is not None
    assert student.name == "Docker Test Student"
    assert any(course.title == "Python" for course in student.courses)


def test_select_students_by_course(db_session):
    """Проверяет выборку студентов, привязанных к определённому курсу."""
    add_student_to_course(
        db_session,
        "Docker Test Select",
        "Docker",
    )

    course = (
        db_session.query(Course)
        .filter_by(title="Docker")
        .first()
    )

    # Собираем имена всех студентов, привязанных к этому курсу
    student_names = [
        student.name
        for student in course.students
    ]

    assert "Docker Test Select" in student_names


def test_update_student_name(db_session):
    """Проверяет изменение имени существующего студента."""
    add_student_to_course(
        db_session,
        "Docker Test Old Name",
        "SQL",
    )

    update_student_name(
        db_session,
        "Docker Test Old Name",
        "Docker Test New Name",
    )

    # Проверяем, что появилась запись с новым именем
    updated_student = (
        db_session.query(Student)
        .filter_by(name="Docker Test New Name")
        .first()
    )

    # Проверяем, что запись со старым именем больше не существует —
    # это подтверждает, что произошло именно ОБНОВЛЕНИЕ записи,
    # а не создание новой рядом со старой
    old_student = (
        db_session.query(Student)
        .filter_by(name="Docker Test Old Name")
        .first()
    )

    assert updated_student is not None
    assert old_student is None


def test_delete_student(db_session):
    """Проверяет удаление существующего студента."""
    add_student_to_course(
        db_session,
        "Docker Test Delete",
        "Git",
    )

    delete_student(
        db_session,
        "Docker Test Delete",
    )

    deleted_student = (
        db_session.query(Student)
        .filter_by(name="Docker Test Delete")
        .first()
    )

    assert deleted_student is None
