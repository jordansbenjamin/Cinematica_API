from main import ma
from schemas.movie_schema import WatchlistMovieSchema


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
            'movies',
        ]


# Singular watchlist schema instance for retreiving a single watchlist
watchlist_schema = WatchlistSchema()
