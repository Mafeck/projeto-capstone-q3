from app.configs.database import db


clients_processes_table = db.Table('clients_processes_table',
                                   db.Column('id', primary_key=True),
                                   db.Column('process_number', db.Integer, db.ForeignKey("processes.number")),
                                   db.Column('client_cpf', db.Integer, db.ForeignKey("clients.cpf"))
                                   )
