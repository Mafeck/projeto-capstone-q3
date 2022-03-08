from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from app.models.client_model import ClientModel
from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientsPhoneModel(db.Model):
    phone: str
    client_cpf: str
    client: ClientModel

    __tablename__ = "clients_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    client_cpf = Column(String, ForeignKey("clients.cpf", ondelete='CASCADE'), nullable=False)

    client = relationship(
        "ClientModel", backref=backref("clients", passive_deletes=True, uselist=False)
    )
