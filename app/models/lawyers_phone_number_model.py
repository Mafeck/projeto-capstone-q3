from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class LawyersPhoneNumber(db.Model):
    phone: str
    lawyer_oab: str

    __tablename__ = "lawyers_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    lawyer_oab = Column(String, ForeignKey("lawyers.oab", ondelete='CASCADE'), nullable=False)

    lawyers = relationship(
        "LawyerModel", backref=backref("lawyers_phone_number", uselist=True), uselist=False
    )
