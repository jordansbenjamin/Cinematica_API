from flask import Blueprint, jsonify, abort
from models.movie import Movie
from schemas.movie_schema import movie_schema, movies_schema

# Initialises flask blueprint with a /movies url prefix
movies_bp = Blueprint('movies', __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["GET"])
def get_all_movies():
    '''GET endpoint/handler for fetching all movies available in the cinematica app'''
    # Query all movie instances from the DB
    movies = Movie.query.all()
    # Serialises queried movie instances from DB with marshmallow schema into Python DST
    response = movies_schema.dump(movies)
    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    '''GET endpoint/handler for fetching specified movie'''
    # Queries specified movie from DB
    movie = Movie.query.filter_by(id=movie_id).first()
    # Checks to see if movie exists
    if not movie:
        # If movie doesn't exist, then return abort message
        return abort(404, description="Movie not found.")
    # Returns jsonified response
    response = movie_schema.dump(movie)
    return jsonify(response), 200
