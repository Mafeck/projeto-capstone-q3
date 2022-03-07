from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.client_model import ClientModel
from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientsPhoneModel(db.Model):
    id: int
    phone: str
    client_cpf: str
    client: ClientModel

    __tablename__ = "client's_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=False)
    client_cpf = Column(String(length=14), ForeignKey("clients.cpf"))

    client = relationship(
        "ClientModel", backref=backref("clients", uselist=False)
    )
