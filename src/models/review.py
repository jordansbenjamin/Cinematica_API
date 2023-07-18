from main import db
from datetime import datetime


class Review(db.Model):
    # Table name for db
    __tablename__ = 'reviews'

    # PK for each movie review
    id = db.Column(db.Integer(), primary_key=True)
    # Body text of movie review
    review_text = db.Column(db.Text(), nullable=False)
    # The movie review's date
    review_date = db.Column(
        db.DateTime(), nullable=False, default=datetime.utcnow)
    # Fk for user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # FK for movie
    movie_id = db.Column(db.Integer, db.ForeignKey(
        'movies.id'), nullable=False)

    # Establishing relationships:

    # Establishing relationship with User and Movie
    user = db.relationship('User', back_populates='reviews')
    movie = db.relationship('Movie', back_populates='reviews')
