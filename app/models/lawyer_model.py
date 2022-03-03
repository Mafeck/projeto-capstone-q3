from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from app.configs.database import db

from dataclasses import dataclass


@dataclass
class LawyerModel(db.Model):
    oab: str
    name: str
    last_name: str
    cpf: str
    email: str
    password_hash: str
    address_id: int

    __tablename__ = "lawyers"

    oab = Column(String, nullable=False, unique=True)
    name = Column(String(length=255))
    last_name = Column(String(length=255))
    cpf = Column(String(length=11), nullable=False, unique=True)
    email = Column(String(length=255), unique=True)
    password_hash = Column(String(length=80), nullable=False)
    address_id = Column(Integer)

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
