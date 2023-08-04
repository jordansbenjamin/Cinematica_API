from controllers.user_controller import users_bp
from controllers.movie_controller import movies_bp
from controllers.watchlist_controller import watchlists_bp
from controllers.movielog_controller import movielogs_bp
from controllers.review_controller import reviews_bp
from controllers.rating_controller import ratings_bp
from controllers.index_controller import index_bp
from controllers.auth_controller import auth_bp

registerable_controllers = [
    index_bp,
    users_bp,
    movies_bp,
    watchlists_bp,
    movielogs_bp,
    reviews_bp,
    ratings_bp,
    auth_bp
]
