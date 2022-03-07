from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel

from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class LawyerModel(db.Model):
    oab: str
    name: str
    last_name: str
    cpf: str
    email: str
    address_id: int
    address: LawyersAddressModel

    __tablename__ = "lawyers"

    oab = Column(String, primary_key=True)
    name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    cpf = Column(String(length=14), nullable=False, unique=True)
    email = Column(String(length=255), nullable=False, unique=True)
    password_hash = Column(String(length=80), nullable=False)
    address_id = Column(Integer, ForeignKey("lawyer's_address.id"), nullable=False, unique=True)

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    lawyers_clients = relationship(
        "ClientModel", secondary="lawyers_clients_table", backref="lawyers"
    )

    address = relationship(
        "LawyersAddressModel", backref("lawyers", uselist=False), uselist=False
    )
