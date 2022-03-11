from app.configs.database import db

clients_comments_table = db.Table('clients_comments_table',
                                    db.Column('id', db.Integer, primary_key=True),
                                    db.Column('client_cpf', db.String, db.ForeignKey("clients.cpf"), nullable=False),
                                    db.Column('comment_id', db.Integer, db.ForeignKey("client_comments.id"), nullable=False)
                                )



