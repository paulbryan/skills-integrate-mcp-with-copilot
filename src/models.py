from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, default="")
    schedule = Column(String, default="")
    max_participants = Column(Integer, default=0)


class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)

