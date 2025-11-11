"""
SQLite via SQLAlchemy ORM.

Why:
- Lightweight now, portable to PostgreSQL later.
"""
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime, logging

Base = declarative_base()
engine = create_engine("sqlite:///app/data/picks.db", echo=False)
Session = sessionmaker(bind=engine)

class PickORM(Base):
    __tablename__ = "picks"
    id = Column(Integer, primary_key=True)
    team = Column(String)
    pick = Column(String)
    confidence = Column(Float, default=0.0)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    processed = Column(Boolean, default=False)

Base.metadata.create_all(engine)

def store_picks(picks, source_id, raw_text):
    log = logging.getLogger("database")
    with Session() as s:
        for p in picks:
            s.add(PickORM(team=p.teams, pick=p.pick))
        s.commit()
        log.info(f"{len(picks)} picks committed to DB.")
