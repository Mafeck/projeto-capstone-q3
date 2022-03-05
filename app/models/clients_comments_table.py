from app.configs.database import db


clients_comments_table = db.Table('clients_comments_table',
                                  db.Column('id', primary_key=True),
                                  db.Column('client_id', db.ForeignKey("clients.id")),
                                  db.Column('comment_id', db.ForeignKey("comments.id")),
                                  )
