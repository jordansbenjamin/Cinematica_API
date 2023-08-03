from main import ma
from marshmallow import fields, validates
from marshmallow.exceptions import ValidationError
from schemas.movie_schema import WatchlistMovieSchema

# MOVIE_ID_ERR_MSG = "List of movie ID's must not be empty"


class WatchlistSchema(ma.Schema):
    # modifying id attribute for changing id field name
    watchlist_id = ma.Integer(attribute="id")
    # Nesting WatchlistMovieSchema to add movies under WatchlistSchema
    movies = ma.Nested(WatchlistMovieSchema, many=True, attribute="movies")

    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'watchlist_id',
            'movies',
        ]


# Singular watchlist schema instance for retreiving a single watchlist
watchlist_schema = WatchlistSchema()


# class BulkAddMoviesSchema(ma.Schema):
#     # Required list of movie ids required in request body
#     list_of_movie_ids = ma.List(ma.Integer(), required=True)

#     @validates('list_of_movie_ids')
#     def validate_movie_ids(self, value):
#         '''Custom method for validating if list of movie id is not empty'''
#         if not value:
#             raise ValidationError(MOVIE_ID_ERR_MSG)


# # Singular bulk add movies schema instance for validating list of movie id's
# bulk_add_movies_schema = BulkAddMoviesSchema()
