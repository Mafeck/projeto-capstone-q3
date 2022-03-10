from app.configs.database import db


clients_processes_table = db.Table('clients_processes_table',
                                   db.Column('id', primary_key=True),
                                   db.Column('process_id', db.Integer, db.ForeignKey("processes.id")),
                                   db.Column('client_cpf', db.Integer, db.ForeignKey("clients.cpf"))
                                   )
