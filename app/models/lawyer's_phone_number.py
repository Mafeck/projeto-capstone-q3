from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


class LawyersPhoneNumber(db.Model):
    id: int
    phone: str
    lawyer_id: int

    __tablename__ = "lawyer's_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String(), nullable=False, unique=True)
    lawyer_id = Column(Integer)

    lawyers = relationship(
        "LawyerModel", backref=backref("lawyer's_phone_number", uselist=True), uselist=False
    )
