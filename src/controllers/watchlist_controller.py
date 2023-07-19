from main import db
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models.watchlist import Watchlist
from models.movie import Movie
from schemas.movie_schema import movie_schema
from schemas.watchlist_schema import watchlist_schema, add_movie_to_watchlist_schema

# Initialises flask blueprint for watchlists, prefix is nested and registered with users bp
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
def get_watchlists(user_id):
    '''GET endpoint/handler for fetching specified users watchlist available in the cinematica app'''
    # Queries watchlist instance from the DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()

    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404

    # Serialises queried watchlist instance from DB with marshmallow schema into Python DST
    result = watchlist_schema.dump(watchlist)
    # Returns the serialised data into JSON format for response
    return jsonify(result), 200


@watchlists_bp.route("/", methods=["POST"])
def add_movie_to_watchlist(user_id):
    '''POST endpoint/handler for adding a movie to a user's watchlist'''
    # Fetch the incoming request data
    data = request.get_json()

    # Validate the data
    errors = add_movie_to_watchlist_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    # Get the movie id
    movie_id = data.get('movie_id')

    # Get the user's watchlist
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404

    # Get the movie
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify(message="Movie not found"), 404

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


@watchlists_bp.route("/", methods=["DELETE"])
def delete_movie_from_watchlist(user_id):
    '''DELETE endpoint/handler for removing a movie from a user's watchlist'''

    # Fetch incoming request data
    data = request.get_json()

    # Get the movie id from the request data
    movie_id = data.get('movie_id')

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