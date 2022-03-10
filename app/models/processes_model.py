from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship,backref

from app.configs.database import db

from dataclasses import dataclass

@dataclass
class ProcessesModel(db.Model):
    
    __tablename__ = "processes"
    
    id: int
    number: int
    
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)