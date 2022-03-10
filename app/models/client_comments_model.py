from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientCommentsModel(db.Model):
    id: int
    comment: str
    create_date: str


    __tablename__ = "client_comments"
    
    id = db.Column(Integer, primary_key=True)
    comment = db.Column(String, nullable=False)
    create_date = db.Column(DateTime, default=datetime.now(), nullable=False)
    
    #comments_rel = relationship(
    #    'ClientModel', backref=backref('client_comments', uselist=True), uselist=False
    #    )
