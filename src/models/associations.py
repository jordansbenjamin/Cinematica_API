from main import db
from datetime import datetime



# This is essentially the join table that connects the relationship between the Movies and Watchlists models.
# It's used because the relationship between these entities is many-to-many, so the association table helps
# bridge this connection. By bringing in together two foreign keys and making them primary keys in this table,
# it ensures that each combination of a movie and a watchlist is unique, or in other words, a specific movie
# can only appear once in a particular watchlist, preventing duplicates of the same movie in the same watchlist.
watchlist_movie_association = db.Table('watchlist_movie_association',
                                       db.Column('watchlist_id', db.Integer, db.ForeignKey(
                                           'watchlists.id'), primary_key=True),
                                       db.Column('movie_id', db.Integer, db.ForeignKey(
                                           'movies.id'), primary_key=True),
                                       db.Column('date_added', db.DateTime(),
                                                 nullable=False, default=datetime.utcnow)
                                       )

# This is the association (also known as junction or join) table for the Movies and MovieLog models.
movielog_movie_association = db.Table('movielog_movie_association', db.Column(
    'movielog_id', db.Integer, db.ForeignKey('movielogs.id'), primary_key=True), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True), db.Column('date_logged', db.DateTime(), nullable=False, default=datetime.utcnow))
