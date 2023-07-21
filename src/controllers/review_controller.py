from main import db
from flask import Blueprint, request, jsonify
from models.review import Review
from models.movie import Movie
from models.user import User
from schemas.review_schema import review_schema, reviews_schema

# Initialises flask blueprint for reviews, prefix is nested and registered with users bp
reviews_bp = Blueprint('reviews', __name__)


@reviews_bp.route("/", methods=["GET"])
def get_reviews(user_id):
    '''GET endpoint/handler for fetching specified users review available in the cinematica app'''
    # Queries user
    user = User.query.get(user_id)
    # If user exists in DB
    if user:
        # Queries review instance from the DB
        reviews = Review.query.filter_by(user_id=user_id).all()
        # Checks if the user has reviews available
        if len(reviews) < 1:
            return jsonify(message="No reviews found, you have not reviewed a movie."), 404
        
        # Serialises queried review instances from DB with marshmallow schema into Python DST
        response = reviews_schema.dump(reviews)
        # Returns the serialised data into JSON format for response
        return jsonify(response), 200
    else:
        return jsonify(message="User does not exist."), 404
    


@reviews_bp.route("/movies/<int:movie_id>/", methods=["POST"])
def create_review(user_id, movie_id):
    '''POST endpoint/handler for adding a movie review for the specified user'''
    review_body_data = review_schema.load(request.json)

    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found."), 404

    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()

    if existing_review:
        return jsonify(message="Review already exists for this movie."), 409

    # Create new review instance
    new_review = Review(
        review_text=review_body_data["review_text"],
        user_id=user_id,
        movie_id=movie_id
    )

    db.session.add(new_review)
    db.session.commit()

    response = review_schema.dump(new_review)
    return jsonify(response), 201


@reviews_bp.route("/movies/<int:movie_id>/", methods=["PUT"])
def update_review(user_id, movie_id):
    '''PUT endpoint/handler for updating a movie review of the specified user'''
    review_body_data = review_schema.load(request.json)

    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found."), 404

    review = Review.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    if not review:
        return jsonify(message="Review not found"), 404

    review.review_text = review_body_data["review_text"]

    db.session.commit()

    response = review_schema.dump(review)

    return jsonify(message="Review sucessfully updated!", review=response), 200


@reviews_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
def delete_review(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie review of the specified user'''
    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found."), 404

    review = Review.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    if not review:
        return jsonify(message="Review not found."), 404

    db.session.delete(review)
    db.session.commit()

    response = review_schema.dump(review)
    return jsonify(message="Review successfully removed!", review=response), 200
