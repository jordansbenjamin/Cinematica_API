from main import db
from flask import Blueprint, jsonify, request
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

    if movie in movielog.movies:
        return jsonify(message="Movie is already in the movielog"), 409

    # Add the movie to the movielog if all else is successful
    movielog.movies.append(movie)

    try:
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        return jsonify(message="Movie successfully added to movielog", movie=movie_data), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify(message="Movie already in movielog"), 400


@movielogs_bp.route("/movies", methods=["PUT"])
def bulk_add_movies_to_movielog(user_id):
    '''PUT endpoint/handler for bulk adding movies to a user's movielog'''

    # Fetch incoming request data
    data = request.get_json()

    # Validate the data (assuming that data is a list of movie ids)
    movie_ids = data.get('list_of_movie_ids')
    if not isinstance(movie_ids, list) or not all(isinstance(i, int) for i in movie_ids):
        return jsonify(message="Invalid data. Expected a list of movie IDs."), 400

    # Get the user's movielog
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    if not movielog:
        return jsonify(message="No movielog found for this user"), 404

    movies_data = []
    already_in_movielog = []
    for movie_id in movie_ids:

        # Get the movie
        movie = Movie.query.get(movie_id)
        if not movie:
            return jsonify(message=f"Movie with id {movie_id} not found"), 404

        # Check if the movie is already in the movielog
        if movie in movielog.movies:
            # Store the movie that's already in movielog
            already_in_movielog.append(movie_schema.dump(movie))
            continue  # Skip to the next movie

        # Add the movie to the movielog
        movielog.movies.append(movie)
        movies_data.append(movie_schema.dump(movie))

    try:
        db.session.commit()

        if len(movies_data) < 1:
            # Include the movie data in the response
            return jsonify(message="These movies are already in the movielog", movies="No movies added", already_in_movielog=already_in_movielog), 200
        elif len(movies_data) > 0 and len(already_in_movielog) > 0:
            # Include the movie data in the response
            return jsonify(message="Movies added to movielog but some are already exists in the movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
        else:
            # Include the movie data in the response
            return jsonify(message="Movies added to movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
    except Exception as error:
        db.session.rollback()
        return jsonify(message=str(error)), 500


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

# NOTE: WILL NEED TO REVISIT THIS CONTROLLER TO CLEAN AND TIGHTEN UP THE LOGIC, ADD VALIDATION, ADD MORE COMMENTS ETC.
