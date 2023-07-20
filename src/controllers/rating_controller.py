from flask import Blueprint, jsonify
from models.rating import Rating
from schemas.rating_schema import rating_schema, ratings_schema

# Initialises flask blueprint for ratings, prefix is nested and registered with users bp
ratings_bp = Blueprint('ratings', __name__)


@ratings_bp.route("/", methods=["GET"])
def get_ratings(user_id):
    '''GET endpoint/handler for fetching specified users movie ratings'''
    # Queries rating instance from the DB
    ratings = Rating.query.filter_by(user_id=user_id).all()
    # Serialises queried rating instances from DB with marshmallow schema into Python DST

    if len(ratings) < 1:
        return jsonify(message="You have not rated a movie yet."), 404

    response = ratings_schema.dump(ratings)
    # Returns the serialised data into JSON format for response
    return jsonify(response)

@ratings_bp.route("/movies/<int:movie_id>/", methods=["POST"])
def add_movie_rating(user_id, movie_id):
    pass