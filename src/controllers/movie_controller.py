from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from main import db
from models.movie import Movie
from schemas.movie_schema import movie_schema, movies_schema, update_movie_schema

# Initialises flask blueprint with a /movies url prefix
movies_bp = Blueprint('movies', __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["GET"])
def get_all_movies():
    '''GET endpoint for fetching all movies available in the cinematica API'''

    # Query all movie instances from the DB
    movies = Movie.query.all()
    # Serialises queried movie instances from DB with marshmallow schema into Python DST
    response = movies_schema.dump(movies)

    # Tally total movies available in DB to include in response
    total_movies = len(movies)
    # Returns the serialised data into JSON format for response
    return jsonify(total_movies=total_movies, movies=response), 200


@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    '''GET endpoint for fetching specified movie'''

    # Queries specified movie instance from DB filtered by movie ID
    movie = Movie.query.filter_by(id=movie_id).first()
    # Checks to see if movie exists in DB
    if not movie:
        # If movie doesn't exist, then return error message
        return jsonify(error=f"Movie with ID of {movie_id} cannot be found, please try again"), 404
    # Returns response as JSON
    response = movie_schema.dump(movie)
    return jsonify(response), 200


@movies_bp.route("/", methods=["POST"])
@jwt_required()
def add_movie():
    '''POST endpoint for creating and adding a new movie'''

    # Validating movie request body data with movie_schema
    try:
        # If successful, load the request body data
        movie_body_data = movie_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Queries existing movie from DB filtered by title and director
    existing_movie = Movie.query.filter_by(
        title=movie_body_data['title'], director=movie_body_data['director']).first()

    # Checks to see if movie exists in DB
    if existing_movie:
        # If movie doesn't exist, then return error message
        return jsonify(error="Movie with the same director already exists, please try again"), 409

    # Create new movie instance
    new_movie = Movie(
        title=movie_body_data.get('title'),
        director=movie_body_data.get('director'),
        genre=movie_body_data.get('genre'),
        runtime=movie_body_data.get('runtime'),
        release_year=movie_body_data.get('release_year')
    )

    # Add new movie instance to DB and commit
    db.session.add(new_movie)
    db.session.commit()
    # Returns new movie information as a JSON respone
    response = movie_schema.dump(new_movie)
    return jsonify(message="Movie successfully added!", new_movie=response), 201


@movies_bp.route("/<int:movie_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_movie(movie_id):
    '''PUT endpoint for updating specified movies info'''

    # Queries specified movie instance from DB filtered by movie_id
    movie = Movie.query.filter_by(id=movie_id).first()
    # Checks to see if movie exists in DB
    if not movie:
        # If movie doesn't exist, then return error message
        return jsonify(error=f"Movie with ID of {movie_id} cannot be found, please try again"), 404

    # Validating movie request body data with update_movie_schema
    try:
        # If successful, load the request body data
        movie_body_data = update_movie_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    def update_title(movie, new_title):
        '''Updates the movie's title'''
        movie.title = new_title

    def update_director(movie, new_director):
        '''Updates the movie's director'''
        movie.director = new_director

    def update_genre(movie, new_genre):
        '''Updates the movie's genre'''
        movie.genre = new_genre

    def update_runtime(movie, new_runtime):
        '''Updates the movie's runtime'''
        movie.runtime = new_runtime

    def update_release_year(movie, new_release_year):
        '''Updates the movie's release_year'''
        movie.release_year = new_release_year

    # Mapping keys to update functions
    updates = {
        "title": update_title,
        "director": update_director,
        "genre": update_genre,
        "runtime": update_runtime,
        "release_year": update_release_year
    }

    # Loops through updates dict to call func for updating movie data
    for field, update_func in updates.items():
        # If the field is present in the request data:
        if field in movie_body_data:
            # Call the corresponding update function with the movie and the new value for the field
            update_func(movie, movie_body_data[field])

    # Checks to see if updated movie is a duplicate
    # Queries DB through filter, excludes current updated movie
    # Checks if both title and directors exists in DB AND matches with updated movie
    existing_movie = Movie.query.filter(
        Movie.id != movie.id,
        Movie.title == movie.title,
        Movie.director == movie.director
    ).first()

    # Checks if the movie already exists in the DB
    if existing_movie:
        # Rolls back changes made if movie is a duplicate
        db.session.rollback()
        return jsonify(error="Movie with the same director and title already exists, please try again."), 409
    else:
        db.session.commit()

    # Save the update movie information for serialisation
    response = movie_schema.dump(movie)
    # Return successful movie update response
    return jsonify(message="Movie successfully updated!", movie=response), 200


@movies_bp.route("/<int:movie_id>", methods=["DELETE"])
@jwt_required()
def delete_movie(movie_id):
    '''DELETE endpoint for deleting specified movie from the Cinematica API'''

    # Queries specified movie instance from DB filtered by movie ID
    movie = Movie.query.filter_by(id=movie_id).first()
    # Checks to see if movie exists in DB
    if not movie:
        # If movie doesn't exist, then return error message
        return jsonify(error=f"Movie with ID of {movie_id} cannot be found, please try again"), 404
    else:
        # If movie exist, then delete movie instance from DB
        db.session.delete(movie)
        db.session.commit()

        return jsonify(message=f"{movie.title} successfully deleted!"), 200
