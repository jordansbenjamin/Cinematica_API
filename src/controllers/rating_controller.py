from flask import Blueprint, jsonify
from models.rating import Rating
from schemas.rating_schema import rating_schema, ratings_schema

# Initialises flask blueprint for ratings, prefix is nested and registered with users bp
ratings_bp = Blueprint('ratings', __name__)


@ratings_bp.route("/", methods=["GET"])
def get_ratings(user_id):
    '''GET endpoint/handler for fetching specified users movie ratings'''
    # Queries rating instance from the DB
    ratings = Rating.query.filter_by(user_id=user_id).first()
    # Serialises queried rating instances from DB with marshmallow schema into Python DST
    response = ratings_schema.dump(ratings)
    # Returns the serialised data into JSON format for response
    return jsonify(response)