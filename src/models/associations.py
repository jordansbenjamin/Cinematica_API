from main import db


watchlist_movie_association = db.Table('watchlist_movie_association', db.Column(
    'watchlist_id', db.Integer, db.ForeignKey('watchlists.id'), nullable=False), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False))

movielog_movie_association = db.Table('movielog_movie_association', db.Column(
    'movielog_id', db.Integer, db.ForeignKey('movielogs.id'), nullable=False), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False))
