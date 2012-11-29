from bottle.ext import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, asc, desc
from globals import Base
import json


class Test(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(Text)
    #__table_args__ = (UniqueConstraint('job_id', 'name', name='_unique_job_and_test_name_'),)
    
    
    def __init__(self, name):
        self.name = name
    
