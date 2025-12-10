from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from infrastructure.database.config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)

# Создаем engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Создание таблиц при старте приложения"""
    try:
        # Импортируем модели здесь, чтобы избежать циклических импортов
        from infrastructure.database.models import FeedbackModel
        Base.metadata.create_all(bind=engine)
        logger.info("All database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        raise