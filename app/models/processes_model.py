from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship,backref
from app.models.clients_process_table import clients_processes_table

from app.configs.database import db

from dataclasses import dataclass

@dataclass
class ProcessesModel(db.Model):
    
    __tablename__ = "processes"
    
    # id: int
    number: str
    description: str
    
    # id = Column(Integer, primary_key=True)
    number = Column(String, primary_key=True)
    description = Column(String, nullable=False)

    clients = relationship(
        "ClientModel",
        secondary=clients_processes_table,
        backref="processes"
    )