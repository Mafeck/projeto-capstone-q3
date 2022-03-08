from sqlalchemy import DateTime, Integer, String, DateTime
from sqlalchemy.orm import relationship,backref
from app.configs.database import db

from dataclasses import dataclass

@dataclass
class ClientCommentsModel(db.Model):
    
    __tablename__ = "client_comments"
    
    id: int
    comment: str
    create_date: DateTime
    
    id = db.Column(Integer, primary_key=True)
    comment = db.Column(String, nullable=False)
    create_date = db.Column(DateTime, nullable=False)
    
    comments_rel = relationship(
        'ClientModel', backref=backref('client_comments', uselist=True), uselist=False
        )