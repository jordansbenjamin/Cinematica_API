from main import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)

    # User's email
    email = db.Colum(db.String(128), nullable=False, unique=True)

    # User's username
    username = db.Column(db.String(64), nullable=False, unique=True)

    # User's password
    password = db.Column(db.String(64), nullable=False)

    # User's join date
    join_date = db.Column(db.DateTime(), default=datetime.utcnow)