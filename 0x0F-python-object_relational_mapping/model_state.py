#!/usr/bin/python3
"""Lists all states from database hbtn_0e_0_usa."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()


class State(Base):
    """Class representing the states table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
