from main import db
from flask import Blueprint, request, jsonify
from models.rating import Rating
from models.movie import Movie
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
    '''POST endpoint/handler for adding a movie rating of the specified user'''

    rating_body_data = rating_schema.load(request.json)

    # Get the movie from DB
    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found"), 404

    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()

    if existing_rating:
        return jsonify(message="Movie already rated"), 409
    
    rating_score = rating_body_data.get("rating_score")

    if not 1 <= rating_score <= 5:
        return jsonify(message="Invalid rating. Rating should be between 1 and 5."), 400

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
    return jsonify(response), 201


@ratings_bp.route("/movies/<int:movie_id>/", methods=["PUT"])
def update_movie_rating(user_id, movie_id):
    '''PUT endpoint/handler for updating a movie's rating of the specified user'''
    rating_body_data = rating_schema.load(request.json)

    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()

    if not existing_rating:
        return jsonify(message="No existing rating found for this movie by this user."), 404
    
    rating_score = rating_body_data.get("rating_score")

    if not 1 <= rating_score <= 5:
        return jsonify(message="Invalid rating. Rating should be between 1 and 5."), 400

    existing_rating.rating_score = rating_body_data["rating_score"]

    db.session.commit()

    response = rating_schema.dump(existing_rating)
    return jsonify(response), 200


@ratings_bp.route("/movies/<int:movie_id>/", methods=["DELETE"])
def remove_movie_rating(user_id, movie_id):
    '''DELETE endpoint/handler for removing a movie rating of the specified user'''
    existing_rating = Rating.query.filter_by(
        user_id=user_id, movie_id=movie_id).first()

    if not existing_rating:
        return jsonify(message="No existing rating found for this movie by this user."), 404

    response = rating_schema.dump(existing_rating)

    db.session.delete(existing_rating)
    db.session.commit()

    return jsonify(message="Movie rating sucessfully removed.", deleted_rating=response), 200
