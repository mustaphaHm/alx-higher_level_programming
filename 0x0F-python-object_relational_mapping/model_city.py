#!/usr/bin/python3
"""Module that use SqlAlchemy ORM instead of MySQL directly."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Definition of class City."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
