from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.client_address_model import ClientAddressModel
from app.configs.database import db

from dataclasses import dataclass


@dataclass
class ClientModel(db.Model):
    cpf: str
    name: str
    last_name: str
    email: str
    password_hash: str
    marital_status: str
    address_id: int
    address: ClientAddressModel

    __tablename__ = "clients"

    cpf = Column(String(length=14), primary_key=True)
    name = Column(String(length=150), nullable=False)
    last_name = Column(String(length=150), nullable=False)
    email = Column(String(length=150), unique=True)
    password_hash = Column(String(length=80))
    marital_status = Column(String(length=20))
    address_id = Column(Integer, ForeignKey("client_address.id"), unique=True)

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    address = relationship(
        "ClientAddressModel", backref=backref("clients", uselist=False), uselist=False
    )
