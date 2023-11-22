from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, Interval
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    registration_date = Column(DateTime, default=datetime.utcnow)


class ConversationHistory(Base):
    __tablename__ = 'conversation_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_message = Column(String)
    bot_reply = Column(String)
    response_duration = Column(Interval)
    created_at = Column(DateTime, default=datetime.utcnow)


DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
