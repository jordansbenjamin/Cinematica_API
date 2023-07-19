from main import db
from datetime import datetime

# REMOVING THIS FOR NOW
# watchlist_movie_association = db.Table('watchlist_movie_association', db.Column(
#     'watchlist_id', db.Integer, db.ForeignKey('watchlists.id'), nullable=False), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False))

# TESTING
watchlist_movie_association = db.Table('watchlist_movie_association',
                                       db.Column('watchlist_id', db.Integer, db.ForeignKey(
                                           'watchlists.id'), primary_key=True),
                                       db.Column('movie_id', db.Integer, db.ForeignKey(
                                           'movies.id'), primary_key=True),
                                       db.Column('date_added', db.DateTime(),
                                                 nullable=False, default=datetime.utcnow)
                                       )


movielog_movie_association = db.Table('movielog_movie_association', db.Column(
    'movielog_id', db.Integer, db.ForeignKey('movielogs.id'), nullable=False), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False))
