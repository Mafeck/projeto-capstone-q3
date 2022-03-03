from app.configs.database import db

from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass
from app.models.client_model import ClientModel
from sqlalchemy.orm import backref, relationship

@dataclass
class ClientsPhoneModel(db.Model):
    id: int
    phone: str
    client: ClientModel

    __tablename__ = "client's_phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)

    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("ClientModel", backref=backref("clients", uselist=False))