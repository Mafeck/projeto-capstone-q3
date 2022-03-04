from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class LawyersPhoneNumber(db.Model):
    id: int
    phone: str
    lawyer_id: int

    __tablename__ = "Lawyer's_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    lawyer_id = Column(Integer, ForeignKey("Lawyers.id"))

    lawyers = relationship(
        "LawyerModel", backref=backref("Lawyer's_phone_number", uselist=True), uselist=False
    )
