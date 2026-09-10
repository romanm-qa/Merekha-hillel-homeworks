from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Строка подключения к PostgreSQL.
# Хост "postgres" — имя сервиса базы данных в docker-compose.yml.
# Контейнеры внутри общей сети Docker Compose могут обращаться
# друг к другу по именам сервисов.
# Порт 5432 — внутренний порт PostgreSQL.
DATABASE_URL = (
    "postgresql+psycopg2://roman:merekharoman@postgres:5432/"
    "student_management"
)

# Подключение SQLAlchemy к базе данных
engine = create_engine(DATABASE_URL)

# Базовый класс для ORM-моделей
Base = declarative_base()

# Фабрика сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)