from main import db
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from models.watchlist import Watchlist
from models.movie import Movie
from models.user import User
from models.associations import watchlist_movie_association
from schemas.movie_schema import movie_schema, minimal_movie_schema
from schemas.watchlist_schema import watchlist_schema
from schemas.bulk_add_movies_schema import bulk_add_movies_schema
from helpers import authenticate_user, check_user_exists

# Initialises flask blueprint for watchlists, prefix is nested and registered with users bp
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
@check_user_exists
def get_watchlist(user_id):
    '''GET endpoint for fetching specified users watchlist available in the cinematica app'''

    # Queries watchlist instance from the DB filtered by ID
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()

    # Queries first instance of user filtered by ID
    user = User.query.filter_by(id=user_id).first()

    # Checks if watchlist exists for the user in the DB
    if not watchlist:
        return jsonify(error=f"No watchlist found for user with ID of {user_id}"), 404
    # Checks if there is a movie in the watchlist
    elif len(watchlist.movies) < 1:
        return jsonify(error=f"No movies found in {user.username}'s watchlist, please try again")

    # Serialises queried watchlist instance from DB with marshmallow schema into Python DST
    response = watchlist_schema.dump(watchlist)

    # Fetch date_added field from the association table in the DB
    for movie_data in response['movies']:
        date_added = db.session.query(watchlist_movie_association.c.date_added)\
            .filter(watchlist_movie_association.c.watchlist_id == watchlist.id)\
            .filter(watchlist_movie_association.c.movie_id == movie_data['movie_id']).first()
        movie_data['added_to_watchlist'] = date_added[0].strftime(
            "%d-%m-%Y") if date_added else None

    # Tally total movies available in the watchlist to include in response
    total_movies = len(watchlist.movies)

    # If there is more than one movie, the response message is plural
    if total_movies > 1:
        # Returns the serialised data into JSON format for response
        return jsonify(total_movies=f"{total_movies} movies in {user.username}'s watchlist", watchlist=response), 200
    else:
        # If there is one movie, the response message is singular
        return jsonify(total_movies=f"{total_movies} movie in {user.username}'s watchlist", watchlist=response), 200


@watchlists_bp.route("/movies/<int:movie_id>", methods=["POST"])
@check_user_exists
@authenticate_user("You are not authorised to add or make changes to this watchlist")
def add_movie_to_watchlist(user_id, movie_id):
    '''POST endpoint for adding a movie to a user's watchlist'''

    # Get the user's watchlist filtered by ID from DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if watchlist exists for the user in the DB
    if not watchlist:
        return jsonify(error=f"No watchlist found for user with ID of {user_id}"), 404

    # Query movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Add the movie to the watchlist
    watchlist.movies.append(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        # Include the movie data in the response
        return jsonify(message=f"{movie.title} successfully added to watchlist", movie=movie_data), 200
    except IntegrityError:
        # Rollback the session if the movie already exists in the watchlist
        db.session.rollback()
        # Return the appropriate error msg
        return jsonify(error=f"{movie.title} is already in this watchlist"), 409


@watchlists_bp.route("/movies", methods=["PUT"])
@check_user_exists
@authenticate_user("You are not authorised to update or make changes to this watchlist")
def bulk_add_movies_to_watchlist(user_id):
    '''PUT endpoint for bulk adding movies to a user's watchlist'''

    # Validating list of movie ID request body data with schema
    try:
        # If successful, load the request body data
        movie_id_list_body_data = bulk_add_movies_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Get the list of movie ID's from the body data
    movie_ids = movie_id_list_body_data.get('list_of_movie_ids')

    # Query the user's watchlist from DB filtered by user ID
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if the watchlist exists for the user in the DB
    if not watchlist:
        return jsonify(error=f"No watchlist found for user with ID of {user_id}"), 404

    # Initialise empty lists
    movies_data = []
    already_in_watchlist = []

    # Iterate movies from list of movie id's
    for movie_id in movie_ids:

        # Query movie from DB based on movie ID
        movie = Movie.query.get(movie_id)
        # Checks if the movie exists
        if not movie:
            return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

        # Check if the movie is already in the watchlist
        if movie in watchlist.movies:
            # Store the movie that's already in watchlist
            already_in_watchlist.append(minimal_movie_schema.dump(movie))
            continue  # Skip to the next movie

        # Add the movie to the watchlist
        watchlist.movies.append(movie)
        # Add the movie to the movie data list
        movies_data.append(minimal_movie_schema.dump(movie))

    try:
        # Commit session to DB
        db.session.commit()

        if len(movies_data) < 1:
            # Include the movie data in the response
            return jsonify(message="These movies are already in the watchlist", already_in_watchlist=already_in_watchlist), 200
        elif len(movies_data) == 1 and len(already_in_watchlist) > 0:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movie added to watchlist but some are already exists in the watchlist", movies=movies_data, already_in_watchlist=already_in_watchlist), 200
        elif len(movies_data) > 1 and len(already_in_watchlist) > 0:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movies added to watchlist but some are already exists in the watchlist", movies=movies_data, already_in_watchlist=already_in_watchlist), 200
        else:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movies added to watchlist", movies=movies_data), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        # Return error message in JSON format
        return jsonify(message=str(error)), 500


@watchlists_bp.route("/movies/<int:movie_id>", methods=["DELETE"])
@check_user_exists
@authenticate_user("You are not authorised to remove or make changes to this watchlist")
def delete_movie_from_watchlist(user_id, movie_id):
    '''DELETE endpoint for removing a movie from a user's watchlist'''

    # Query the user's watchlist from the DB filtered by user_id
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Checks if the watchlist exists for the user in the DB
    if not watchlist:
        return jsonify(error=f"No watchlist found for user with ID of {user_id}"), 404

    # Query the movie from DB based on movie_id
    movie = Movie.query.get(movie_id)
    # Check if the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Check if the movie is in the watchlist
    if movie not in watchlist.movies:
        return jsonify(error=f"{movie.title} not found in watchlist to remove"), 400

    # If successful, remove the movie from the watchlist
    watchlist.movies.remove(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        # Include the movie data in the response
        return jsonify(message=f"{movie.title} sucessfully removed from watchlist", movie=movie_data), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        # Return error message in JSON format
        return jsonify(message=str(error)), 500
