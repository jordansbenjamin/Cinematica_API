from main import db
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from models.rating import Rating
from models.movie import Movie
from models.user import User
from schemas.rating_schema import rating_schema, ratings_schema
from helpers import authenticate_user

# Initialises flask blueprint for ratings, prefix is nested and registered with users bp
ratings_bp = Blueprint('ratings', __name__)


@ratings_bp.route("/", methods=["GET"])
def get_ratings(user_id):
    '''GET endpoint/handler for fetching specified users movie ratings'''

    # Query the user using get by user_id from DB
    user = User.query.get(user_id)

    # Checks if user exists in DB
    if user:
        # Queries rating instance from DB
        ratings = Rating.query.filter_by(user_id=user_id).all()

        # Checks if there are movies rated
        if len(ratings) < 1:
            return jsonify(message=f"No ratings found for user with ID of {user_id}, please try again"), 404

        # Serialises queried rating instances from DB with marshmallow schema into Python DST
        response = ratings_schema.dump(ratings)
        # Returns the serialised data into JSON format for response
        return jsonify(message=f"{len(ratings)} movies rated for {user.username}", ratings=response)
    else:
        return jsonify(message=f"User with ID of {user_id} cannot be found"), 404


@ratings_bp.route("/movies/<int:movie_id>/", methods=["POST"])
@authenticate_user("You are not authorised to add or make changes to this users ratings")
def add_movie_rating(user_id, movie_id):
    '''POST endpoint/handler for adding a movie rating of the specified user'''

    # Validating rating request body data with schema
    try:
        # If successful, load the request body data
        rating_body_data = rating_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing rating for a movie from DB filtered by both user_id and movie_id
    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a rating for a mvovie already exists to avoid duplication
    if existing_rating:
        return jsonify(message=f"{movie.title} has already been rated"), 409

    # Create new rating instance
    new_rating = Rating(
        rating_score=rating_body_data["rating_score"],
        user_id=user_id,
        movie_id=movie_id
    )

    # Add and commit new movie rating to DB
    db.session.add(new_rating)
    db.session.commit()

    # Return the new rating as a JSON response
    response = rating_schema.dump(new_rating)
    return jsonify(message=f"{movie.title} added to ratings!", rating=response), 201


@ratings_bp.route("/movies/<int:movie_id>/", methods=["PUT"])
@authenticate_user("You are not authorised to update or make changes to this users ratings")
def update_movie_rating(user_id, movie_id):
    '''PUT endpoint/handler for updating a movie's rating of the specified user'''

    # Validating rating request body data with schema
    try:
        # If successful, load the request body data
        rating_body_data = rating_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing rating for a movie from DB filtered by both user_id and movie_id
    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a rating for a movie already exists for the rating to be updated
    if not existing_rating:
        return jsonify(message=f"No existing rating found for {movie.title} by user with ID of {user_id}"), 404

    # Update the existing rating with the new rating
    existing_rating.rating_score = rating_body_data["rating_score"]

    # Commit updated changes to DB
    db.session.commit()

    # Return the updated rating as a JSON response
    response = rating_schema.dump(existing_rating)
    return jsonify(message=f" Rating for {movie.title} successfully updated!", rating=response), 200


@ratings_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
@authenticate_user("You are not authorised to remove or make changes to this users ratings")
def remove_movie_rating(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie rating of the specified user'''

    # Query movie from DB based on movie id
    movie = Movie.query.get(movie_id)
    # Checks if the movie exists
    if not movie:
        return jsonify(message=f"Movie with ID {movie_id} cannot be found, please try again"), 404

    # Query an existing rating for a movie from DB filtered by both user_id and movie_id
    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()
    # Checks if a rating for a movie already exists for the rating to be removed
    if not existing_rating:
        return jsonify(message=f"No existing rating found for {movie.title} by user with ID of {user_id}"), 404

    # Save rating before deletion for response
    response = rating_schema.dump(existing_rating)

    # Delete exisiting rating and commit changes to DB
    db.session.delete(existing_rating)
    db.session.commit()

    # Return message and deleted_rating response as JSON
    return jsonify(message=f"{movie.title} sucessfully removed!", deleted_rating=response), 200
