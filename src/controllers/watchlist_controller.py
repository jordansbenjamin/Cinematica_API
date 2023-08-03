from main import db
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from models.watchlist import Watchlist
from models.movie import Movie
from models.associations import watchlist_movie_association
from schemas.movie_schema import movie_schema
from schemas.watchlist_schema import watchlist_schema, bulk_add_movies_schema

# Initialises flask blueprint for watchlists, prefix is nested and registered with users bp
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
def get_watchlist(user_id):
    '''GET endpoint/handler for fetching specified users watchlist available in the cinematica app'''

    # Queries watchlist instance from the DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()

    # Checks if watchlist exists for theuser
    if not watchlist:
        return jsonify(message=f"No watchlist found for user of ID {user_id}"), 404
    # Checks if there is a movie in the watchlist
    elif len(watchlist.movies) < 1:
        return jsonify(message="No movies found in this watchlist, please add a movie")

    # Serialises queried watchlist instance from DB with marshmallow schema into Python DST
    response = watchlist_schema.dump(watchlist)

    # Fetch date_added field from the association table
    for movie_data in response['movies']:
        date_added = db.session.query(watchlist_movie_association.c.date_added)\
            .filter(watchlist_movie_association.c.watchlist_id == watchlist.id)\
            .filter(watchlist_movie_association.c.movie_id == movie_data['movie_id']).first()
        movie_data['added_to_watchlist'] = date_added[0].strftime(
            "%Y-%m-%d") if date_added else None

    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@watchlists_bp.route("/movies/<int:movie_id>", methods=["POST"])
def add_movie_to_watchlist(user_id, movie_id):
    '''POST endpoint/handler for adding a movie to a user's watchlist'''

    # Get the user's watchlist filtered by user id from DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if watchlist exists for the user
    if not watchlist:
        return jsonify(message=f"No watchlist found for user of ID {user_id}"), 404

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} not found"), 404

    # Add the movie to the watchlist
    watchlist.movies.append(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)

        # Include the movie data in the response
        return jsonify(message=f"{movie.title} added to watchlist", movie=movie_data), 200
    except IntegrityError:
        # Rollback the session if the movie already exists in the watchlist
        db.session.rollback()
        return jsonify(message=f"{movie.title} is already in watchlist"), 409


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

    # Get the list of movie id's from the body data
    movie_ids = movie_id_list_body_data.get('list_of_movie_ids')

    # Get the user's watchlist
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if the watchlist exists for the user
    if not watchlist:
        return jsonify(message=f"No watchlist found for this user with ID of {user_id}"), 404

    # Initialise empty lists
    movies_data = []
    already_in_watchlist = []

    # Iterate movies from list of movie id's
    for movie_id in movie_ids:

        # Query movie from DB based on movie id
        movie = Movie.query.get(movie_id)
        # Checks if the movie exists
        if not movie:
            return jsonify(message=f"Movie with ID {movie_id} not found"), 404

        # Check if the movie is already in the watchlist
        if movie in watchlist.movies:
            # Store the movie that's already in watchlist
            already_in_watchlist.append(movie_schema.dump(movie))
            continue  # Skip to the next movie

        # Add the movie to the watchlist
        watchlist.movies.append(movie)
        # Add the movie to the movie data list
        movies_data.append(movie_schema.dump(movie))

    try:
        # Commit session to DB
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
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        return jsonify(message=str(error)), 500


@watchlists_bp.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie_from_watchlist(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie from a user's watchlist'''

    # Get the user's watchlist from the DB filtered by user id
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if the watchlist exists for the user
    if not watchlist:
        return jsonify(message="No watchlist found for this user"), 404

    # Get the movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Check if the move exists
    if not movie:
        return jsonify(message="Movie not found"), 404

    # Check if the movie is in the watchlist
    if movie not in watchlist.movies:
        return jsonify(message="Movie not in watchlist"), 400

    # Remove the movie from the watchlist
    watchlist.movies.remove(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)

        # Include the movie data in the response
        return jsonify(message="Movie sucessfully removed from watchlist", movie=movie_data), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        return jsonify(message=str(error)), 500
