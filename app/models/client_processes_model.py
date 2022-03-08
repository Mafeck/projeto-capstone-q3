from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship,backref
from app.configs.database import db

from dataclasses import dataclass

@dataclass
class ClientProcessesModel(db.Model):
    
    __tablename__ = "client_processes"
    
    id: int
    number: int
    
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    
    processes_rel = relationship(
        'ClientModel', backref=backref('client_processes', uselist=True), uselist=False
    )