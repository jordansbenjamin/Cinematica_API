from main import ma
from marshmallow import validates
from marshmallow.exceptions import ValidationError

MOVIE_ID_ERR_MSG = "List of movie ID's must not be empty, please try again"

class BulkAddMoviesSchema(ma.Schema):
    # Required list of movie ids required in request body
    list_of_movie_ids = ma.List(ma.Integer(), required=True)

    @validates('list_of_movie_ids')
    def validate_movie_ids(self, value):
        '''Custom method for validating if list of movie id is not empty'''
        if not value:
            raise ValidationError(MOVIE_ID_ERR_MSG)


# Singular bulk add movies schema instance for validating list of movie id's
bulk_add_movies_schema = BulkAddMoviesSchema()