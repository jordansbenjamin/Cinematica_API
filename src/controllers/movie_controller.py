from flask import Blueprint, jsonify, request, abort
from marshmallow.exceptions import ValidationError
from main import db
from models.movie import Movie
from schemas.movie_schema import movie_schema, movies_schema

# Initialises flask blueprint with a /movies url prefix
movies_bp = Blueprint('movies', __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["GET"])
def get_all_movies():
    '''GET endpoint/handler for fetching all movies available in the cinematica API'''
    # Query all movie instances from the DB
    movies = Movie.query.all()
    # Serialises queried movie instances from DB with marshmallow schema into Python DST
    response = movies_schema.dump(movies)
    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    '''GET endpoint/handler for fetching specified movie'''
    # Queries specified movie from DB
    movie = Movie.query.filter_by(id=movie_id).first()
    # Checks to see if movie exists
    if not movie:
        # If movie doesn't exist, then return abort message
        return abort(404, description="Movie not found.")
    # Returns jsonified response
    response = movie_schema.dump(movie)
    return jsonify(response), 200


@movies_bp.route("/", methods=["POST"])
def add_movie():
    '''POST route/handler for creating and adding a new movie'''
    # NOTE: Use exception handling to validate the fields loaded from the request body is provided
    movie_body_data = movie_schema.load(request.json)
    # Queries existing movie filtered by title and director
    existing_movie = Movie.query.filter_by(
        title=movie_body_data['title'], director=movie_body_data['director']).first()

    if existing_movie:
        return abort(409, description="Movie with the same director already exists, please try again.")

    # Create new Movie instance
    new_movie = Movie(
        title=movie_body_data.get('title'),
        director=movie_body_data.get('director'),
        genre=movie_body_data.get('genre'),
        runtime=movie_body_data.get('runtime'),
        release_year=movie_body_data.get('release_year'),
    )

    # Add new movie instance to db and commit
    db.session.add(new_movie)
    db.session.commit()
    # Returns new movie information as a JSON respone
    response = movie_schema.dump(new_movie)
    return jsonify(response), 201


@movies_bp.route("/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    '''PUT route/handler for updating specified movies info'''
    movie = Movie.query.filter_by(id=movie_id).first()

    try:
        movie_body_data = movie_schema.load(request.json)
    except ValidationError as error:
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

    # For each item (field, update function pair) in the 'updates' dict:
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

    if existing_movie:
        # Rolls back changes made if movie is a dupe
        db.session.rollback()
        return abort(409, description="Movie with the same director and title already exists, please try again.")
    else:
        db.session.commit()

    response = movie_schema.dump(movie)
    return jsonify(response), 200


@movies_bp.route("/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    '''DELETE route/handler for deleting specified movie from the Cinematica API'''
    # Queries movie from DB
    movie = Movie.query.filter_by(id=movie_id).first()

    if not movie:
        return abort(404, description="Movie not found.")
    else:
        # Save movie data before deleting
        movie_data = movie_schema.dump(movie)
        # If movie exist, then delete movie instance from DB
        db.session.delete(movie)
        db.session.commit()
        # Create custom response message
        response = {
            "message": "Movie successfully deleted!",
            "deleted_movie": movie_data
        }
        return jsonify(response), 200
