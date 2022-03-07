from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates

from osirisvalidator.string import not_blank
from osirisvalidator.internet import valid_email

from app.configs.database import db
from app.exc import lawyer_exception, oab_name_last_name_exception

import re
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

    id = Column(Integer, primary_key=True)
    oab = Column(String, nullable=False, unique=True)
    name = Column(String(length=255))
    last_name = Column(String(length=255))
    cpf = Column(String(length=14), nullable=False, unique=True)
    email = Column(String(length=255), nullable=False, unique=True)
    password_hash = Column(String(length=511), nullable=False)
    address_id = Column(Integer, ForeignKey("Lawyer's_address.id"))

    """
    lawyers_clients = relationship(
        "ClientModel", secundary="Lawyers_clients_table", backref="Lawyers"
    )
    """

    @property
    def password(self):
        raise AttributeError("Inaccessible password!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password_hash(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)


    @validates('email')
    @not_blank(field='email')
    @valid_email(field='email')
    def validate_email(self, _, email):
        return email

    @validates('cpf')
    def validate_cpf(self, _, cpf):
        pattern = "(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)"

        if not re.search(pattern, cpf):
            raise lawyer_exception.CpfFormatException(
                "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
            )
        return cpf
    
    @validates('oab', 'name', 'last_name')
    def validate_oab_name_last_name(self, key, value):
        if type(value) != str:
            raise oab_name_last_name_exception.OabNameLastNameException(
                "'oab', 'name' and 'last_name' must be a string type."
            )
        return value
    