from main import db
from datetime import datetime
from sqlalchemy import CheckConstraint


class Rating(db.Model):
    # Table name for db
    __tablename__ = 'ratings'

    # PK for ratings
    id = db.Column(db.Integer(), primary_key=True)
    # Holds the movies score rating
    rating_score = db.Column(db.Integer(), nullable=False)
    # The date the movie is rated
    rating_date = db.Column(
        db.DateTime(), nullable=False, default=datetime.utcnow)
    # Fk for user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # FK for movie
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    # Establishing relationships:
    
    # Establishing relationship with User and Movie
    user = db.relationship('User', back_populates='rating')
    movie = db.relationship('Movie', back_populates='ratings')

    # Constraint for rating score (1-5) on database level
    # __table_args__ = (
    #     CheckConstraint('rating_score>=1 AND rating_score<=5',
    #                     name='rating_score_check')
    # )
