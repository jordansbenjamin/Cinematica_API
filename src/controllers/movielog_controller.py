from main import db
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from models.movie import Movie
from models.movielog import MovieLog
from models.associations import movielog_movie_association
from schemas.movie_schema import movie_schema
from schemas.movielog_schema import movielog_schema
from schemas.bulk_add_movies_schema import bulk_add_movies_schema

# Initialises flask blueprint for movielogs, prefix is nested and registered with users bp
movielogs_bp = Blueprint('movielogs', __name__)


@movielogs_bp.route("/", methods=["GET"])
def get_movielogs(user_id):
    '''GET endpoint/handler for fetching specified users movielog available in the cinematica app'''

    # Queries movielog instance from the DB
    movielog = MovieLog.query.filter_by(user_id=user_id).first()

    # Checks if movielog exists for the user
    if not movielog:
        return jsonify(message=f"No movielog found for user with ID of {user_id}"), 404
    # Checks if there is a movie in the movielog
    elif len(movielog.movies) < 1:
        return jsonify(message="No movies found in this movielog, please add a movie")

    # Serialises queried movielog instance from DB with marshmallow schema into Python DST
    response = movielog_schema.dump(movielog)

    # Fetch date_logged field from the association table
    for movie_data in response['movies']:
        date_logged = db.session.query(movielog_movie_association.c.date_logged)\
            .filter(movielog_movie_association.c.movielog_id == movielog.id)\
            .filter(movielog_movie_association.c.movie_id == movie_data['movie_id']).first()
        movie_data['added_to_movielog'] = date_logged[0].strftime(
            "%d-%m-%Y") if date_logged else None

    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@movielogs_bp.route("/movies/<int:movie_id>/", methods=["POST"])
def add_movie_to_movielog(user_id, movie_id):
    '''POST endpoint/handler for adding a movie to a user's movielog'''

    # Queries movielog filtered by user_id
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if movielog exists for the user
    if not movielog:
        return jsonify(message=f"No movielog found for user with ID of {user_id}"), 404

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Add the movie to the movielog if all else is successful
    movielog.movies.append(movie)

    try:
        # Commit changes to DB & serialise movie for response
        db.session.commit()
        movie_data = movie_schema.dump(movie)
        # Include the movie data in the response
        return jsonify(message=f"{movie.title} added to movielog", movie=movie_data), 200
    except IntegrityError:
        # Rollback the session if the movie already exists in the watchlist
        db.session.rollback()
        return jsonify(message=f"{movie.title} is already in this movielog"), 409


@movielogs_bp.route("/movies", methods=["PUT", "PATCH"])
def bulk_add_movies_to_movielog(user_id):
    '''PUT endpoint/handler for bulk adding movies to a user's movielog'''

    # Validating list of movie ID request body data with schema
    try:
        # If successful, load the request body data
        movie_id_list_body_data = bulk_add_movies_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Get the list of movie id's from the body data
    movie_ids = movie_id_list_body_data.get('list_of_movie_ids')

    # Get the user's movielog
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if the movielog exists for the user
    if not movielog:
        return jsonify(message=f"No movielog found for user with ID of {user_id}"), 404

    # Initialise empty lists
    movies_data = []
    already_in_movielog = []
    for movie_id in movie_ids:

        # Query movie from DB based on movie ID
        movie = Movie.query.get(movie_id)
        # Checks if the movie exists
        if not movie:
            return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

        # Check if the movie is already in the movielog
        if movie in movielog.movies:
            # Store the movie that's already in movielog
            already_in_movielog.append(movie_schema.dump(movie))
            continue  # Skip to the next movie

        # Add the movie to the movielog
        movielog.movies.append(movie)
        # Add the movie to the movie data list
        movies_data.append(movie_schema.dump(movie))

    try:
        # Commit session to DB
        db.session.commit()

        # Checks to see if there are new movies to be added to movielog if movies_data is empty
        if len(movies_data) < 1:
            # If true, it means no movies will be added to movielog
            return jsonify(message="These movies are already in the movielog", movies="No movies added", already_in_movielog=already_in_movielog), 200
        # Checks to see if both movies_data and already_in_movielog contains movies
        elif len(movies_data) > 0 and len(already_in_movielog) > 0:
            # If true, then movies are added but also show already added movies in the movielog in the response
            return jsonify(message="Movies added to movielog but some are already exists in the movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
        # All else, movies that haven't been added to movielog will be added accordingly
        else:
            # Include the movie data in the response
            return jsonify(message="Movies added to movielog", movies=movies_data, already_in_movielog=already_in_movielog), 200
    except Exception as error:
        # Rollback the session and changes made if there is an error
        db.session.rollback()
        # Return error message in JSON format
        return jsonify(message=str(error)), 500


@movielogs_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
def remove_movie_from_movielog(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie from a user's movielog'''

    # Query the user's movielog from the DB filtered by user_id
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Checks if the movielog exists for the user
    if not movielog:
        return jsonify(message=f"No watchlist found for user with ID of {user_id}"), 404

    # Query the movie from DB based on movie_id
    movie = Movie.query.get(movie_id)
    # Check is the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Checks if the movie is in the movielog
    if movie not in movielog.movies:
        return jsonify(message="Movie not found in movielog to remove"), 400

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
        return jsonify(message=str(error)), 500
