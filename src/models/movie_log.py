from main import db
from datetime import datetime

class MovieLog(db.Model):
    # Table name for db
    __tablename__ = 'movie_logs'

    # PK for each movie entry in the movie log
    id = db.Column(db.Integer(), primary_key=True)
    # Date movie is added to the movie log
    log_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    # Establishing relationships:
    # WILL DO LATER