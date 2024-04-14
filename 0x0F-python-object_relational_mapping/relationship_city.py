#!/usr/bin/python3
"""list all states in the table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
