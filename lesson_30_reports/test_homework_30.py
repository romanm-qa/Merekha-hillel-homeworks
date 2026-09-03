import allure
import pytest
from sqlalchemy import text

from database import Base, SessionLocal, engine
from homework_30 import (
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
    test_students = (session.query(Student).filter(Student.name.like("Docker Test%")).all())

    for student in test_students:
        session.delete(student)

    session.commit()

    yield session

    # Очищаем созданные тестами данные
    test_students = (session.query(Student).filter(Student.name.like("Docker Test%")).all())

    for student in test_students:
        session.delete(student)

    session.commit()
    session.close()


@allure.feature("Database connection")
def test_database_connection(db_session):
    """Проверяет, что соединение с базой данных работает."""

    with allure.step("Execute a test SQL query"):
        result = db_session.execute(text("SELECT 1"))

    with allure.step("Verify the database response"):
        assert result.scalar() == 1


@allure.feature("Student management")
def test_add_student_to_course(db_session):
    """Проверяет добавление студента и его привязку к курсу."""

    with allure.step("Add a student to the Python course"):
        add_student_to_course(db_session, "Docker Test Student", "Python")

    with allure.step("Find the created student in the database"):
        student = (db_session.query(Student).filter_by(name="Docker Test Student").first())

    with allure.step("Verify the student and course data"):
        assert student is not None
        assert student.name == "Docker Test Student"
        assert any(course.title == "Python" for course in student.courses)


@allure.feature("Student management")
def test_select_students_by_course(db_session):
    """Проверяет выборку студентов, привязанных к определённому курсу."""

    with allure.step("Add a student to the Docker course"):
        add_student_to_course(db_session, "Docker Test Select", "Docker")

    with allure.step("Get students assigned to the Docker course"):
        course = (db_session.query(Course).filter_by(title="Docker").first())

        # Собираем имена всех студентов, привязанных к этому курсу
        student_names = [student.name for student in course.students]

    with allure.step("Verify that the student belongs to the course"):
        assert "Docker Test Select" in student_names


@allure.feature("Student management")
def test_update_student_name(db_session):
    """Проверяет изменение имени существующего студента."""

    with allure.step("Add a student with the original name"):
        add_student_to_course(db_session, "Docker Test Old Name", "SQL")

    with allure.step("Update the student's name"):
        update_student_name(db_session, "Docker Test Old Name", "Docker Test New Name")

    with allure.step("Get student records after the update"):
        updated_student = (db_session.query(Student).filter_by(name="Docker Test New Name").first())

        old_student = (db_session.query(Student).filter_by(name="Docker Test Old Name").first())

    with allure.step("Verify that the student name was updated"):
        assert updated_student is not None

        # Проверяем, что запись со старым именем больше не существует —
        # это подтверждает, что произошло именно обновление записи,
        # а не создание новой рядом со старой
        assert old_student is None


@allure.feature("Student management")
def test_delete_student(db_session):
    """Проверяет удаление существующего студента."""

    with allure.step("Add a student to be deleted"):
        add_student_to_course(db_session, "Docker Test Delete", "Git")

    with allure.step("Delete the student"):
        delete_student(db_session, "Docker Test Delete")

    with allure.step("Search for the deleted student in the database"):
        deleted_student = (db_session.query(Student).filter_by(name="Docker Test Delete").first())

    with allure.step("Verify that the student no longer exists"):
        assert deleted_student is None
