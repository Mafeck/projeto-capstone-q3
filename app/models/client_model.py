from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from app.configs.database import db
from app.models.client_address_model import ClientAddressModel

from werkzeug.security import generate_password_hash, check_password_hash


class ClientModel(db.Model):
    address: ClientAddressModel

    __tablename__ = "clients"

    cpf = Column(String(length=14), primary_key=True)
    name = Column(String(length=150), nullable=False)
    last_name = Column(String(length=150), nullable=False)
    email = Column(String(length=150), unique=True, nullable=False)
    password_hash = Column(String(length=255))
    marital_status = Column(String(length=20), nullable=False)
    address_id = Column(Integer, ForeignKey("client_address.id"), nullable=False)

    address = relationship(
        "ClientAddressModel", backref=backref("address", uselist=False), uselist=False
    )

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
