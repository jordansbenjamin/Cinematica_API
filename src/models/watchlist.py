from main import db
from datetime import datetime

class Watchlist(db.Model):
    __tablename__ = 'watchlists'

    id = db.Column(db.Integer(), primary_key=True)
    date_added = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    
    # Establishing relationships:
    # WILL DO LATER