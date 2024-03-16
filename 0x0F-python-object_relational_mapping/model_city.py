#!/usr/bin/python3
"""This module is for city"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """City class represents a city entity.

    Attributes:
        id (int): Unique identifier for the city.
        name (str): Name of the city.
        state_id (int): Foreign key referencing the
        state to which the city belongs."""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
