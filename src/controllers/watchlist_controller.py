from main import db
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from models.watchlist import Watchlist
from models.movie import Movie
from schemas.movie_schema import movie_schema
from schemas.watchlist_schema import watchlist_schema, bulk_add_movies_schema

# Initialises flask blueprint for watchlists, prefix is nested and registered with users bp
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
def get_watchlist(user_id):
    '''GET endpoint/handler for fetching specified users watchlist available in the cinematica app'''
    # Queries watchlist instance from the DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()

    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404
    
    if len(watchlist.movies) < 1:
        return jsonify(message="No movies found in this watchlist, please add a movie")

    # Serialises queried watchlist instance from DB with marshmallow schema into Python DST
    response = watchlist_schema.dump(watchlist)
    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@watchlists_bp.route("/movies/<int:movie_id>", methods=["POST"])
def add_movie_to_watchlist(user_id, movie_id):
    '''POST endpoint/handler for adding a movie to a user's watchlist'''

    # Get the user's watchlist
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404

    # Get the movie
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify(message="Movie not found"), 404

    if movie in watchlist.movies:
        return jsonify(message="Movie is already in the watchlist"), 409

    # Add the movie to the watchlist
    watchlist.movies.append(movie)

    try:
        db.session.commit()
        movie_data = movie_schema.dump(movie)

        # Include the movie data in the response
        return jsonify(message="Movie added to watchlist", movie=movie_data), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify(message="Movie already in watchlist"), 400


@watchlists_bp.route("/movies", methods=["PUT"])
def bulk_add_movies_to_watchlist(user_id):
    '''PUT endpoint/handler for bulk adding movies to a user's watchlist'''

    # Validating list of movie ID request body data with schema
    try:
        # If successful, load the request body data
        movie_id_list_body_data = bulk_add_movies_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    movie_ids = movie_id_list_body_data.get('list_of_movie_ids')

    # Get the user's watchlist
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    if not watchlist:
        return jsonify(message=f"No watchlist found for this user with ID of {user_id}"), 404

    movies_data = []
    already_in_watchlist = []
    for movie_id in movie_ids:

        # Get the movie
        movie = Movie.query.get(movie_id)
        if not movie:
            return jsonify(message=f"Movie with ID {movie_id} not found"), 404

        # Check if the movie is already in the watchlist
        if movie in watchlist.movies:
            already_in_watchlist.append(movie_schema.dump(movie))  # Store the movie that's already in watchlist
            continue  # Skip to the next movie

        # Add the movie to the watchlist
        watchlist.movies.append(movie)
        movies_data.append(movie_schema.dump(movie))

    try:
        db.session.commit()

        if len(movies_data) < 1:
            # Include the movie data in the response
            return jsonify(message="These movies are already in the watchlist", movies="No movies added", already_in_watchlist=already_in_watchlist), 200
        elif len(movies_data) > 0 and len(already_in_watchlist) > 0:
            # Include the movie data in the response
            return jsonify(message="Movies added to watchlist but some are already exists in the watchlist", movies=movies_data, already_in_watchlist=already_in_watchlist), 200
        else:
            # Include the movie data in the response
            return jsonify(message="Movies added to watchlist", movies=movies_data), 200
    except Exception as error:
        db.session.rollback()
        return jsonify(message=str(error)), 500



@watchlists_bp.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie_from_watchlist(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie from a user's watchlist'''

    # Get the user's watchlist
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404

    # Get the movie
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify(message="Movie not found"), 404

    # Check if the movie is in the watchlist
    if movie not in watchlist.movies:
        return jsonify(message="Movie not in watchlist"), 400

    # Remove the movie from the watchlist
    watchlist.movies.remove(movie)

    try:
        db.session.commit()
        movie_data = movie_schema.dump(movie)

        # Include the movie data in the response
        return jsonify(message="Movie sucessfully removed from watchlist", movie=movie_data), 200
    except Exception as error:
        db.session.rollback()
        return jsonify(message=str(error)), 500

# NOTE: WILL NEED TO REVISIT THIS CONTROLLER TO CLEAN AND TIGHTEN UP THE LOGIC, ADD VALIDATION, ETC.
