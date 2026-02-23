from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from datetime import datetime

from app.db.session import Base


class CountryCovid(Base):
    __tablename__ = "country_covid"

    id = Column(Integer, primary_key=True, index=True)

    # Datos principales
    country = Column(String(100), unique=True, nullable=False, index=True)
    continent = Column(String(50))

    # Estadísticas
    cases = Column(BigInteger)
    deaths = Column(BigInteger)
    recovered = Column(BigInteger)
    active = Column(BigInteger)
    population = Column(BigInteger)
    last_updated = Column(BigInteger)

    # Extra
    flag = Column(String(255))
    updated_at = Column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow)

    # Auditoría
    created_at = Column(DateTime, default=datetime.utcnow)