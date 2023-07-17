from main import db
from datetime import datetime


class User(db.Model):
    # NOTE:
    # Class attrbute to associate model class with db table
    # Considered good practice to include
    # Otherwise SQLAlchemy will automatically generate it
    # Converts PascalCase class model name to snake_case db name

    # Table name for db
    __tablename__ = 'users'

    # Sets the user's PK
    id = db.Column(db.Integer(), primary_key=True)
    # User's email
    email = db.Column(db.String(128), nullable=False, unique=True)
    # User's username
    username = db.Column(db.String(64), nullable=False, unique=True)
    # User's password
    password = db.Column(db.String(64), nullable=False)
    # User's date joined
    join_date = db.Column(db.Date(), default=datetime.utcnow)

    # Establishing relationships:
    
    # Establishes one-to-one relationship with Watchlist and MovieLog models
    watchlist = db.relationship('Watchlist', back_populates='user', uselist=False, cascade='all, delete')
    movielog = db.relationship('MovieLog', back_populates='user', uselist=False, cascade='all, delete')
    # NOTE: SQLAlchemy sets relationships by default as one-to-many
    # uselist=False changes this behaviour so it becomes one-to-one

    # Establishes one-to-many relationship with Review and Rating models
    review = db.relationship('Review', back_populates='user', cascade='all, delete')
    rating = db.relationship('Rating', back_populates='user', cascade='all, delete')