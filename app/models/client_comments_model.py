from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.orm import relationship
from app.models.clients_comments_table import clients_comments_table

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientCommentsModel(db.Model):
    id: int
    comment: str
    create_date: str
    update_at: str

    __tablename__ = "client_comments"
    
    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    title = Column(String, default='Title', nullable=False)
    create_date = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime, default=datetime.now(), nullable=False)
    
    clients = relationship(
        "ClientModel", secondary=clients_comments_table, backref="comments"
    )
