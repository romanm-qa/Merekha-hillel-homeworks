from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Строка подключения к PostgreSQL
DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres@localhost:5433/"
    "student_management"
)

# Подключение SQLAlchemy к базе данных
engine = create_engine(DATABASE_URL)

# Базовый класс для ORM-моделей
Base = declarative_base()

# Фабрика сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)
