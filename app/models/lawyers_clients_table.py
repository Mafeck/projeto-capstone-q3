from app.configs.database import db


lawyers_clients_table = db.Table('lawyers_clients_table',
                                 db.Column('id', db.Integer, primary_key=True),
                                 db.Column('lawyer_oab', db.Integer, db.ForeignKey("lawyers.oab"), nullable=False),
                                 db.Column('client_cpf', db.Integer, db.ForeignKey("clients.cpf"), nullable=False),
                                 )
