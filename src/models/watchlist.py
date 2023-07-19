from main import db
from datetime import datetime
from models.associations import watchlist_movie_association


class Watchlist(db.Model):
    # Table name for db
    __tablename__ = 'watchlists'

    # PK for each movie entry in the watchlist
    id = db.Column(db.Integer(), primary_key=True)
    # REMOVING THIS FOR NOW
    # Date movie is added to the watchlist
    # date_added = db.Column(db.DateTime(), nullable=False,
    #                        default=datetime.utcnow)
    # FK for user
    # unique parameter set to True to enforce one-to-one relation
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False, unique=True)

    # Establishing relationships:

    # Establishes (one-to-one) relationship with user
    user = db.relationship('User', back_populates='watchlist')

    # Establishes many-to-many relationship with Movie model through association table
    movies = db.relationship(
        'Movie', secondary=watchlist_movie_association, back_populates='watchlists')
