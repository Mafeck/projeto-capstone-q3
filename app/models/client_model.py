from sqlalchemy.orm import backref, relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey
from osirisvalidator.string import not_blank
from osirisvalidator.internet import valid_email

from app.configs.database import db
from app.models.client_address_model import ClientAddressModel
from app.exc import exceptions

import re
from dataclasses import dataclass


@dataclass
class ClientModel(db.Model):
    cpf: str
    name: str
    last_name: str
    email: str
    marital_status: str
    address_id: int
    address: ClientAddressModel

    __tablename__ = "clients"

    cpf = Column(String(length=14), primary_key=True)
    name = Column(String(length=150), nullable=False)
    last_name = Column(String(length=150), nullable=False)
    email = Column(String(length=150), unique=True, nullable=False)
    marital_status = Column(String(length=20), nullable=False)
    address_id = Column(Integer, ForeignKey("client_address.id"), nullable=False)

    address = relationship(
        "ClientAddressModel", backref=backref("clients", uselist=False), uselist=False
    )

    @validates('email')
    @not_blank(field='email')
    @valid_email(field='email')
    def validate_email(self, _, email):
        return email

    @validates('cpf')
    def validate_cpf(self, _, cpf):
        pattern = "(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)"

        if not re.search(pattern, cpf):
            raise exceptions.CpfFormatException(
                "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
            )
        return cpf

    @validates('name', 'last_name', 'marital_status')
    def validate_name_last_name_marital_status(self, key, value):
        if type(value) != str:
            raise exceptions.TypeException(
                "'name','last_name' and 'marital_status' must be a string type."
            )
        return value
