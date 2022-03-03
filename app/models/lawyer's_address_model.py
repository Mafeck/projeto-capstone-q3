from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


class LawyersAddressModel(db.Model):
    id: int
    street: str
    number: int
    district: str
    state: str
    country: str
    cep: str

    __tablename__ = "Lawyer's_address"

    id = Column(Integer, primary_key=True)
    street = Column(String(length=255), nullable=False)
    number = Column(String(length=10))
    district = Column(String(length=255), nullable=False)
    state = Column(String(length=255), nullable=False)
    country = Column(String(length=255), nullable=False)
    cep = Column(String(length=255), nullable=False)

    lawyers = relationship(
        "LawyersModel", backref=backref("Lawyer's_address", uselist=False), uselist=False
    )
