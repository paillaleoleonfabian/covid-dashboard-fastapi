from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

#url de conn a Postgres
DATABASE_URL = settings.database_url

#conn principal
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

#sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#modelos
Base = declarative_base()