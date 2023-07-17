from flask import Blueprint, jsonify
from models.review import Review
from schemas.review_schema import review_schema, reviews_schema

# Initialises flask blueprint for reviews, prefix is nested and registered with users bp
reviews_bp = Blueprint('reviews', __name__)


@reviews_bp.route("/", methods=["GET"])
def get_reviews(user_id):
    '''GET endpoint/handler for fetching specified users review available in the cinematica app'''
    # Queries review instance from the DB
    reviews = Review.query.filter_by(user_id=user_id).all()
    # Serialises queried review instances from DB with marshmallow schema into Python DST
    result = reviews_schema.dump(reviews)
    # Returns the serialised data into JSON format for response
    return jsonify(result)