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
# COMMENTED OUT BECAUSE TECHNICALLY A USER ONLY HAS ONE WATCHLIST
# WILL DELETE IN THE FUTURE, KEEPING IT JUST IN CASE
# # Multiple watchlists schema instance for retreiving multiple watchlists
# watchlists_schema = WatchlistSchema(many=True)


class WatchlistAddSchema(ma.Schema):
    movie_id = fields.Int(required=True)


add_movie_to_watchlist_schema = WatchlistAddSchema()
