from app.configs.database import db

from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass
from app.models.client_address_model import ClientAddressModel
from sqlalchemy.orm import backref, relationship

@dataclass
class ClientModel(db.Model):
    cpf: str
    name: str
    last_name: str
    email: str
    password_hash: str
    marital_status: str
    address: ClientAddressModel

    __tablename__ = "clients"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password_hash = Column(String)
    marital_status = Column(String)

    address_id = Column(Integer, ForeignKey("client_address.id"))

    address = relationship("ClientAddressModel", backref=backref("client_address", uselist=False))