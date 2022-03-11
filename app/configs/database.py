from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.db = db

    from app.models.lawyer_model import LawyerModel
    from app.models.lawyers_address_model import LawyersAddressModel
    from app.models.lawyers_phone_number_model import LawyersPhoneNumber
    from app.models.client_model import ClientModel
    from app.models.client_address_model import ClientAddressModel
    from app.models.clients_phone_number_model import ClientsPhoneModel
    from app.models.lawyers_clients_table import lawyers_clients_table
    from app.models.client_comments_model import ClientCommentsModel
    from app.models.clients_comments_table import clients_comments_table
    from app.models.clients_process_table import clients_processes_table
