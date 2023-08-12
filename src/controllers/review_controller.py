from main import db
from flask import Blueprint, request, jsonify
from marshmallow.exceptions import ValidationError
from models.review import Review
from models.movie import Movie
from models.user import User
from schemas.review_schema import review_schema, reviews_schema
from helpers import authenticate_user, check_user_exists

# Initialises flask blueprint for reviews, prefix is nested and registered with users bp
reviews_bp = Blueprint('reviews', __name__)


@reviews_bp.route("/", methods=["GET"])
def get_reviews(user_id):
    '''GET endpoint for fetching specified users review available in the cinematica app'''

    # Queries user instance from DB filtered by user ID
    user = User.query.get(user_id)

    # Checks if user exists in DB
    if user:
        # Queries review instance from the DB
        reviews = Review.query.filter_by(user_id=user_id).all()
        # Checks if the user have existing reviews available
        if len(reviews) < 1:
            return jsonify(error=f"No reviews found for {user.username}, please try again"), 404

        # Serialises queried review instances from DB with marshmallow schema into Python DST
        response = reviews_schema.dump(reviews)
        if len(reviews) > 1:
            # Returns the serialised data into JSON format for response
            return jsonify(message=f"{len(reviews)} movies reviewed for {user.username}", ratings=response)
        else:
            # For singular response message
            return jsonify(message=f"{len(reviews)} movie reviewed for {user.username}", ratings=response)
    else:
        return jsonify(error=f"User with ID of {user_id} cannot be found, please try again"), 404


@reviews_bp.route("/movies/<int:movie_id>/", methods=["POST"])
@check_user_exists
@authenticate_user("You are not authorised to add or make changes to this users reviews")
def create_review(user_id, movie_id):
    '''POST endpoint for adding a movie review for the specified user'''

    # Validating review request body data with schema
    try:
        # If successful, load the request body data
        review_body_data = review_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user ID and movie ID
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if existing_review:
        return jsonify(error=f"{movie.title} has already been reviewed"), 409

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
    return jsonify(message=f"{movie.title} added to ratings!", review=response), 201


@reviews_bp.route("/movies/<int:movie_id>/", methods=["PUT"])
@check_user_exists
@authenticate_user("You are not authorised to update or make changes to this users reviews")
def update_review(user_id, movie_id):
    '''PUT endpoint for updating a movie review of the specified user'''

    # Validating review request body data with schema
    try:
        # If successful, load the request body data
        review_body_data = review_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user ID and movie ID
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if not existing_review:
        return jsonify(error=f"No existing review found for {movie.title}"), 404

    # Update the existing review with the new review
    existing_review.review_text = review_body_data["review_text"]

    # Commit updated changes to DB
    db.session.commit()

    # Return the updated review as a JSON response
    response = review_schema.dump(existing_review)
    return jsonify(message=f"Review for {movie.title} sucessfully updated!", review=response), 200


@reviews_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
@check_user_exists
@authenticate_user("You are not authorised to remove or make changes to this users reviews")
def delete_review(user_id, movie_id):
    '''DELETE endpoint for removing a movie review of the specified user'''

    # Query movie from DB based on movie ID
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists in the DB
    if not movie:
        return jsonify(error=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing review for a movie from DB filtered by both user ID and movie ID
    existing_review = Review.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a review for a movie already exists to avoid duplication
    if not existing_review:
        return jsonify(error=f"No existing review found for {movie.title}"), 404

    # Save review before deletion for response
    response = review_schema.dump(existing_review)

    # Delete exisiting review and commit changes to DB
    db.session.delete(existing_review)
    db.session.commit()

    # Return message and deleted_review response as JSON
    return jsonify(message="Review successfully removed!", deleted_review=response), 200
