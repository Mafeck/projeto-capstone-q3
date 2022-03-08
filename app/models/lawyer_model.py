from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref, validates
from osirisvalidator.string import not_blank
from osirisvalidator.internet import valid_email

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.exc import lawyer_exception

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
    address: LawyersAddressModel

    __tablename__ = "lawyers"

    oab = Column(String, primary_key=True)
    name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    cpf = Column(String(length=14), nullable=False, unique=True)
    email = Column(String(length=255), nullable=False, unique=True)
    password_hash = Column(String(length=255), nullable=False)
    address_id = Column(Integer, ForeignKey("lawyers_address.id"), nullable=False)

    lawyers_clients = relationship(
        "LawyerModel", secondary="lawyers_clients_table", backref="lawyers"
    )

    address = relationship(
        "LawyersAddressModel", backref=backref("lawyers", uselist=False), uselist=False
    )

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
            raise lawyer_exception.OabNameLastNameException(
                "'oab', 'name' and 'last_name' must be a string type."
            )
        return value
