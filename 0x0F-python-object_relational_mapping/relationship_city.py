#!/usr/bin/python3
"""
This script contains the class definition of a City
"""
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        state_id (str): integer, cant be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)