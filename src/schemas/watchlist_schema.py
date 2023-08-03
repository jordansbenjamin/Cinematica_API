from main import ma
from marshmallow import fields, validates
from marshmallow.exceptions import ValidationError
from schemas.movie_schema import WatchlistMovieSchema

MOVIE_ID_ERR_MSG = "List of movie ID's must not be empty"


class WatchlistSchema(ma.Schema):
    watchlist_id = fields.Integer(attribute="id")
    movies = fields.Nested(WatchlistMovieSchema, many=True, attribute="movies")

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


class BulkAddMoviesSchema(ma.Schema):

    list_of_movie_ids = fields.List(fields.Integer(), required=True)

    @validates('list_of_movie_ids')
    def validate_movie_ids(self, value):
        if not value:
            raise ValidationError(MOVIE_ID_ERR_MSG)


bulk_add_movies_schema = BulkAddMoviesSchema()
