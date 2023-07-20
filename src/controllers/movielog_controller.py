from main import db
from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError
from models.movie import Movie
from models.movielog import MovieLog
from schemas.movie_schema import movie_schema
from schemas.movielog_schema import movielog_schema

# Initialises flask blueprint for movielogs, prefix is nested and registered with users bp
movielogs_bp = Blueprint('movielogs', __name__)


@movielogs_bp.route("/", methods=["GET"])
def get_movielogs(user_id):
    '''GET endpoint/handler for fetching specified users movielog available in the cinematica app'''
    # Queries movielog instance from the DB
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Serialises queried movielog instance from DB with marshmallow schema into Python DST
    result = movielog_schema.dump(movielog)
    # Returns the serialised data into JSON format for response
    return jsonify(result)


@movielogs_bp.route("/movies/<int:movie_id>/", methods=["POST"])
def add_movie_to_movielog(user_id, movie_id):
    '''POST endpoint/handler for adding a movie to a user's movielog'''
    # NOTE: I removed the need for the movielog_id in the actual route path
    # Because its inferred that a movielog belongs to the user via the user_id
    # This will be checked via jWt

    # Queries movielog filtered by user_id
    movielog = MovieLog.query.filter_by(user_id=user_id).first()

    if not movielog:
        return jsonify(message="Movielog not found for this user"), 404

    # Getting the movie
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify(message="Movie not found."), 404

    # Add the movie to the movielog if all else is successful
    movielog.movies.append(movie)

    try:
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        return jsonify(message="Movie successfully added to movielog", movie=movie_data), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify(message="Movie already in movielog"), 400

@movielogs_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
def remove_movie_from_movielog(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie from a user's movielog'''
    movielog = MovieLog.query.filter_by(user_id=user_id).first()

    if not movielog:
        return jsonify(message="Movielog not found for this user"), 404

    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found"), 404
    
    if movie not in movielog.movies:
        return jsonify(message="Movie not found in movielog to remove"), 400
    
    movielog.movies.remove(movie)

    try:
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        return jsonify(message="Movie successfully removed from movielog!", movie=movie_data), 200
    except Exception as error:
        db.session.rollback()
        return jsonify(message=str(error)), 500