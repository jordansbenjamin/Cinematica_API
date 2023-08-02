from main import ma
from marshmallow import fields
from schemas.movie_schema import WatchlistMovieSchema


class WatchlistSchema(ma.Schema):
    movies = fields.Nested(WatchlistMovieSchema, many=True, attribute="movies")

    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'movies',
        ]


# Singular watchlist schema instance for retreiving a single watchlist
watchlist_schema = WatchlistSchema()
