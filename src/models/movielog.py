from main import db
from datetime import datetime
from models.associations import movielog_movie_association


class MovieLog(db.Model):
    # Table name for db
    __tablename__ = 'movielogs'

    # PK for each movie entry in the movie log
    id = db.Column(db.Integer(), primary_key=True)
    # REMOVING THIS SIMILAR TO WATCHLIST
    # # Date movie is added to the movie log
    # log_date = db.Column(db.DateTime(), nullable=False,
    #                      default=datetime.utcnow)

    # FK for user
    # unique parameter set to True to enforce one-to-one relation
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False, unique=True)

    # Establishing relationships:

    # Establishes (one-to-one) relationship with user
    user = db.relationship('User', back_populates='movielog')

    # Establishes many-to-many relationship with Movie model through association table
    movies = db.relationship(
        'Movie', secondary=movielog_movie_association, back_populates='movielogs')
