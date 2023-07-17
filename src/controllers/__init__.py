from user_controller import users_bp
from movie_controller import movies_bp
from watchlist_controller import watchlists_bp
from movielog_controller import movielogs_bp
from review_controller import reviews_bp
from rating_controller import ratings_bp

registerable_controllers = [
    users_bp,
    movies_bp,
    watchlists_bp,
    movielogs_bp,
    reviews_bp,
    ratings_bp,
]