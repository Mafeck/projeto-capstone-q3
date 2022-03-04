from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.configs.database import db

from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class LawyerModel(db.Model):
    oab: str
    name: str
    last_name: str
    cpf: str
    email: str
    address_id: dict

    __tablename__ = "Lawyers"

    oab = Column(String, nullable=False, unique=True)
    name = Column(String(length=255))
    last_name = Column(String(length=255))
    cpf = Column(String(length=11), nullable=False, unique=True)
    email = Column(String(length=255), nullable=False, unique=True)
    password_hash = Column(String(length=80), nullable=False)
    address_id = Column(Integer, ForeignKey("Lawyer's_address.id"))

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    lawyers_clients = relationship(
        "ClientModel", secundary="lawyers_clients_table", backref="lawyers"
    )
