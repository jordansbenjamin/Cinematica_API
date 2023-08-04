from main import db
from flask import Blueprint, request, jsonify
from marshmallow.exceptions import ValidationError
from models.review import Review
from models.movie import Movie
from models.user import User
from schemas.review_schema import review_schema, reviews_schema

# Initialises flask blueprint for reviews, prefix is nested and registered with users bp
reviews_bp = Blueprint('reviews', __name__)


@reviews_bp.route("/", methods=["GET"])
def get_reviews(user_id):
    '''GET endpoint/handler for fetching specified users review available in the cinematica app'''

    # Queries user instance from DB
    user = User.query.get(user_id)

    # Checks if user exists in DB
    if user:
        # Queries review instance from the DB
        reviews = Review.query.filter_by(user_id=user_id).all()
        # Checks if the user has reviews available
        if len(reviews) < 1:
            return jsonify(message=f"No reviews found for user with ID of {user_id}, please try again"), 404

        # Serialises queried review instances from DB with marshmallow schema into Python DST
        response = reviews_schema.dump(reviews)
        # Returns the serialised data into JSON format for response
        return jsonify(message=f"{len(reviews)} movies reviewed for {user.username}", ratings=response)
    else:
        return jsonify(message=f"User with ID of {user_id} cannot be found, please try again"), 404


@reviews_bp.route("/movies/<int:movie_id>/", methods=["POST"])
def create_review(user_id, movie_id):
    '''POST endpoint/handler for adding a movie review for the specified user'''

    # Queries user instance from DB
    user = User.query.get(user_id)
    # Return response message if user cannot be found
    if not user:
        return jsonify(message=f"User with ID of {user_id} cannot be found, please try again"), 404

    # Validating review request body data with schema
    try:
        # If successful, load the request body data
        review_body_data = review_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user_id and movie_id
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if existing_review:
        return jsonify(message=f"{movie.title} has already been reviewed"), 409

    # Create new review instance
    new_review = Review(
        review_text=review_body_data["review_text"],
        user_id=user_id,
        movie_id=movie_id
    )

    # Add and commit new movie review to DB
    db.session.add(new_review)
    db.session.commit()

    # Return the new rating as a JSON response
    response = review_schema.dump(new_review)
    return jsonify(response), 201


@reviews_bp.route("/movies/<int:movie_id>/", methods=["PUT"])
def update_review(user_id, movie_id):
    '''PUT endpoint/handler for updating a movie review of the specified user'''

    # Queries user instance from DB
    user = User.query.get(user_id)
    # Return response message if user cannot be found
    if not user:
        return jsonify(message=f"User with ID of {user_id} cannot be found, please try again"), 404

    # Validating review request body data with schema
    try:
        # If successful, load the request body data
        review_body_data = review_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user_id and movie_id
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if not existing_review:
        return jsonify(message=f"No existing review found for {movie.title} by user with ID of {user_id}"), 404

    # Update the existing review with the new review
    existing_review.review_text = review_body_data["review_text"]

    # Commit updated changes to DB
    db.session.commit()

    # Return the updated review as a JSON response
    response = review_schema.dump(existing_review)
    return jsonify(message="Review sucessfully updated!", review=response), 200


@reviews_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
def delete_review(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie review of the specified user'''

    # Queries user instance from DB
    user = User.query.get(user_id)
    # Return response message if user cannot be found
    if not user:
        return jsonify(message=f"User with ID of {user_id} cannot be found, please try again"), 404

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user_id and movie_id
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if not existing_review:
        return jsonify(message=f"No existing review found for {movie.title} by user with ID of {user_id}"), 404

    # Save review before deletion for response
    response = review_schema.dump(existing_review)

    # Delete exisiting review and commit changes to DB
    db.session.delete(existing_review)
    db.session.commit()

    # Return message and deleted_review response as JSON
    return jsonify(message="Review successfully removed!", deleted_review=response), 200
