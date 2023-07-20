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
    '''POST endpoint/handler for adding a movie rating for the specified user'''

    rating_body_data = rating_schema.load(request.json)

    # Get the movie from DB
    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify(message="Movie not found"), 404
    
    existing_rating = Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    if existing_rating:
        return jsonify(message="Movie already rated"), 409

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


