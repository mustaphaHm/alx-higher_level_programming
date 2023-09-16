#!/usr/bin/python3
"""Module that use SqlAlchemy ORM instead of MySQL directly."""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Definition of class State."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
