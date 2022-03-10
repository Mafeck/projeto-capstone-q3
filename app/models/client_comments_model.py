from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.orm import relationship, backref
from app.models.clients_comments_table import clients_comments_table

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientCommentsModel(db.Model):
    id: int
    comment: str
    create_date: str


    __tablename__ = "client_comments"
    
    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    create_date = Column(DateTime, default=datetime.now(), nullable=False)
    
    clients = relationship(
        "ClientModel",
        secondary=clients_comments_table,
        backref="comments"
    )

    #comments_rel = relationship(
    #    'ClientModel', backref=backref('client_comments', uselist=True), uselist=False
    #    )
