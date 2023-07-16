from main import db
from datetime import datetime

class Watchlist(db.Model):
    # Table name for db
    __tablename__ = 'watchlists'

    # PK for each movie entry in the watchlist
    id = db.Column(db.Integer(), primary_key=True)
    # Date movie is added to the watchlist
    date_added = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    
    # Establishing relationships:
    # WILL DO LATER