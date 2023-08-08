from main import db
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from models.movie import Movie
from models.movielog import MovieLog
from models.user import User
from models.associations import movielog_movie_association
from schemas.movie_schema import movie_schema, minimal_movie_schema
from schemas.movielog_schema import movielog_schema
from schemas.bulk_add_movies_schema import bulk_add_movies_schema
from helpers import authenticate_user, check_user_exists

# Initialises flask blueprint for movielogs, prefix is nested and registered with users bp
movielogs_bp = Blueprint('movielogs', __name__)


@movielogs_bp.route("/", methods=["GET"])
@check_user_exists
def get_movielogs(user_id):
    '''GET endpoint for fetching specified users movielog available in the cinematica app'''

    # Queries movielog instance from the DB filtered by ID
    movielog = MovieLog.query.filter_by(user_id=user_id).first()

    # Queries first instance of user filtered by ID
    user = User.query.filter_by(id=user_id).first()

    # Checks if movielog exists for the user in the DB
    if not movielog:
        return jsonify(error=f"No movielog found for user with ID of {user_id}"), 404
    # Checks if there is a movie in the movielog
    elif len(movielog.movies) < 1:
        return jsonify(error=f"No movies found in {user.username}'s movielog, please try again")

    # Serialises queried movielog instance from DB with marshmallow schema into Python DST
    response = movielog_schema.dump(movielog)

    # Fetch date_logged field from the association table
    for movie_data in response['movies']:
        date_logged = db.session.query(movielog_movie_association.c.date_logged)\
            .filter(movielog_movie_association.c.movielog_id == movielog.id)\
            .filter(movielog_movie_association.c.movie_id == movie_data['movie_id']).first()
        movie_data['added_to_movielog'] = date_logged[0].strftime(
            "%d-%m-%Y") if date_logged else None

    # Tally total movies available in the watchlismovielog to include in response
    total_movies = len(movielog.movies)

    # If there is more than one movie, the response message is plural
    if total_movies > 1:
        # Returns the serialised data into JSON format for response
        return jsonify(total_movies=f"{total_movies} movies in {user.username}'s movielog", movielog=response), 200
    else:
        # If there is one movie, the response message is singular
        return jsonify(total_movies=f"{total_movies} movie in {user.username}'s movielog", movielog=response), 200


@movielogs_bp.route("/movies/<int:movie_id>/", methods=["POST"])
@check_user_exists
@authenticate_user("You are not authorised to add or make changes to this movielog")
def add_movie_to_movielog(user_id, movie_id):
    '''POST endpoint for adding a movie to a user's movielog'''

    # Queries movielog from DB filtered by user ID
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if movielog exists for the user in the DB
    if not movielog:
        return jsonify(error=f"No movielog found for user with ID of {user_id}"), 404

    # Query movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists in the movielog
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Add the movie to the movielog if all else is successful
    movielog.movies.append(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        # Include the movie data in the response
        return jsonify(message=f"{movie.title} added to movielog", movie=movie_data), 200
    except IntegrityError:
        # Rollback the session if the movie already exists in the movielog
        db.session.rollback()
        return jsonify(error=f"{movie.title} is already in this movielog"), 409


@movielogs_bp.route("/movies", methods=["PUT", "PATCH"])
@check_user_exists
@authenticate_user("You are not authorised to update or make changes to this movielog")
def bulk_add_movies_to_movielog(user_id):
    '''PUT endpoint for bulk adding movies to a user's movielog'''

    # Validating list of movie ID request body data with schema
    try:
        # If successful, load the request body data
        movie_id_list_body_data = bulk_add_movies_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Get the list of movie id's from the body data
    movie_ids = movie_id_list_body_data.get('list_of_movie_ids')

    # Query the user's movielog filtered by user ID
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if the movielog exists for the user
    if not movielog:
        return jsonify(error=f"No movielog found for user with ID of {user_id}"), 404

    # Initialise empty lists
    movies_data = []
    already_in_movielog = []

    # Iterate movies from list of movie id's
    for movie_id in movie_ids:

        # Query movie from DB based on movie ID
        movie = Movie.query.get(movie_id)
        # Checks if the movie exists in the DB
        if not movie:
            return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

        # Check if the movie is already in the movielog
        if movie in movielog.movies:
            # Store the movie that's already in the movielog to the already_in_movielog list
            already_in_movielog.append(minimal_movie_schema.dump(movie))
            continue  # Skip to the next movie

        # Add the movie to the users movielog
        movielog.movies.append(movie)
        # Add the movie to the movie data list
        movies_data.append(minimal_movie_schema.dump(movie))

    try:
        # Commit session to DB
        db.session.commit()

        if len(movies_data) < 1:
            # Include the movie data in the response
            return jsonify(message="These movies are already in the movielog", already_in_movielog=already_in_movielog), 200
        elif len(movies_data) == 1 and len(already_in_movielog) > 0:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movie added to movielog but some are already exists in the movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
        elif len(movies_data) > 1 and len(already_in_movielog) > 0:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movies added to movielog but some are already exists in the movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
        else:
            # Include the movie data in the response
            return jsonify(message=f"{len(movies_data)} movies added to movielog", movies=movies_data), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        # Return error message in JSON format
        return jsonify(error=str(error)), 500


@movielogs_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
@check_user_exists
@authenticate_user("You are not authorised to remove or make changes to this movielog")
def remove_movie_from_movielog(user_id, movie_id):
    '''DELETE endpoint for removing a movie from a user's movielog'''

    # Query the user's movielog from the DB filtered by user ID
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if the movielog exists for the user
    if not movielog:
        return jsonify(error=f"No movielog found for user with ID of {user_id}"), 404

    # Query the movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Check is the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Checks if the movie is in the movielog
    if movie not in movielog.movies:
        return jsonify(error=f"{movie.title} not found in movielog to remove"), 400

    # Remove the movie from the movielog
    movielog.movies.remove(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        # Include the movie data in the response
        return jsonify(message=f"{movie.title} successfully removed from movielog!", movie=movie_data), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        # Return error message in JSON format
        return jsonify(error=str(error)), 500
