from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from app.models.lawyer_model import LawyerModel

from dataclasses import dataclass


@dataclass
class LawyersPhoneNumber(db.Model):
    id: int
    phone: str
    lawyer_oab: str
    lawyers: LawyerModel

    __tablename__ = "lawyer's_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    lawyer_oab = Column(String, ForeignKey("lawyers.oab"))

    lawyers = relationship(
        "LawyerModel", backref=backref("lawyer's_phone_number", uselist=True), uselist=False
    )
