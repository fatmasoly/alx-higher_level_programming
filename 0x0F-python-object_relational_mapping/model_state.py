#!/usr/bin/python3
"""This module is for state"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class representing the 'states' table in the database.

    Attributes:
    -----------
    __tablename__ : states
        Name of the table in the database.

    id : Column
        Integer column representing the primary key of the state.

    name : Column
        String column representing the name of the state."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
