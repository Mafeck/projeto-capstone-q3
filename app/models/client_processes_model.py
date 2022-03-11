from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.clients_process_table import clients_processes_table

from app.configs.database import db

from dataclasses import dataclass

@dataclass
class ProcessesModel(db.Model):

    number: str
    description: str
    
    __tablename__ = "processes"
    
    number = Column(String, primary_key=True)
    description = Column(String, nullable=False)

    clients = relationship(
        "ClientModel",
        secondary=clients_processes_table,
        backref="processes"
    )