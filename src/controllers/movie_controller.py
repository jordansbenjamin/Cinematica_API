from flask import Blueprint, jsonify
from models.movie import Movie
from schemas.movie_schema import movie_schema, movies_schema

# Initialises flask blueprint with a /movies url prefix
movies_bp = Blueprint('movies', __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["GET"])
def get_movies():
    '''GET endpoint/handler for fetching all movies available in the cinematica app'''
    # Query all movie instances from the DB
    movies = Movie.query.all()
    # Serialises queried movie instances from DB with marshmallow schema into Python DST
    result = movies_schema.dump(movies)
    # Returns the serialised data into JSON format for response
    return jsonify(result)
