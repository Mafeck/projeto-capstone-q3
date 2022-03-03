from app.configs.database import db

from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class ClientAddressModel(db.Model):
    id: int
    street: str
    district: str
    state: str
    country: str
    cep: str

    __tablename__ = "client_address"

    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    district = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    cep = Column(String, nullable=False, unique=True)