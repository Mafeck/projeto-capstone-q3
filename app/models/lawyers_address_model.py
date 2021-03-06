from sqlalchemy import Column, Integer, String

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class LawyersAddressModel(db.Model):
    street: str
    number: int
    district: str
    state: str
    country: str
    cep: str

    __tablename__ = "lawyers_address"

    id = Column(Integer, primary_key=True)
    street = Column(String(length=255), nullable=False)
    number = Column(String(length=10), nullable=False)
    district = Column(String(length=255), nullable=False)
    state = Column(String(length=255), nullable=False)
    country = Column(String(length=255), nullable=False)
    cep = Column(String(length=255), nullable=False)
