from main import db
from models.associations import watchlist_movie_association, movielog_movie_association


class Movie(db.Model):
    # Table name for db
    __tablename__ = 'movies'

    # Sets the movies PK
    id = db.Column(db.Integer(), primary_key=True)
    # Movie's title
    title = db.Column(db.String(128), nullable=False)
    # Movie's director
    director = db.Column(db.String(64), nullable=False)
    # Movie's genre
    genre = db.Column(db.String(32), nullable=False)
    # Movie's runtime
    runtime = db.Column(db.String(16), nullable=False)
    # Movie's release date
    release_year = db.Column(db.Integer(), nullable=False)

    # Establishing relationships:

    # Establishes many-to-many relationship with Watchlist and MovieLog models
    # Note: Secondary parameter tells SQLAlchemy to use association table for handling many-to-many
    watchlists = db.relationship(
        'Watchlist', secondary=watchlist_movie_association, back_populates='movies')
    movielogs = db.relationship(
        'MovieLog', secondary=movielog_movie_association, back_populates='movies')

    # Establishes one-to-many relationship with Review and Rating models
    reviews = db.relationship('Review', back_populates='movie')
    ratings = db.relationship('Rating', back_populates='movie')
