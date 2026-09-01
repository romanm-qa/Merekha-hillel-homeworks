from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Строка подключения к PostgreSQL.
# Хост "hw29_postgres" — это ИМЯ КОНТЕЙНЕРА с базой данных.
# Работает только внутри Docker-сети (когда оба контейнера
# запущены с --network и видят друг друга по имени).
# Порт 5432 — "родной" (внутренний) порт Postgres,
# а не тот, что проброшен наружу для доступа с компьютера.
DATABASE_URL = (
    "postgresql+psycopg2://roman:merekharoman@hw29_postgres:5432/"
    "student_management"
)

# Подключение SQLAlchemy к базе данных
engine = create_engine(DATABASE_URL)

# Базовый класс для ORM-моделей
Base = declarative_base()

# Фабрика сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)
