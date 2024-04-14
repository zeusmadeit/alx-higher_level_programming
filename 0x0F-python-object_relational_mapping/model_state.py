#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))