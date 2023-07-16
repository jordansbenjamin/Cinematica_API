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

    # Establishing relationships:
    # WILL DO LATER

    # Constraint for rating score (1-5)
    __table_args__ = (
        CheckConstraint('rating_score>=1 AND rating_score<=5',
                        name='rating_score_check')
    )
