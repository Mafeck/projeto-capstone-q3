from app.configs.database import db


lawyers_clients_table = db.Table('lawyers_clients_table',
                                 db.Column('id', db.Integer, primary_key=True),
                                 db.Column('lawyer_oab', db.Integer, nullable=False),
                                 db.Column('client_cpf', db.Integer, nullable=False)
                                 )
