from main import ma
from marshmallow import fields, validate, pre_load

VALID_GENRES = ('Drama', 'Action', 'Comedy', 'Sci-fi', 'Thriller', 'Superhero', 'Romance', 'Horror', 'Adventure', 'Animation', 'Fantasy', 'Musical', 'Mystery', 'Family', 'Crime', 'Documentary', 'Western', 'Biographical', 'War', 'Film-noir')
RUNTIME_ERR_MSG = "Runtime must be in the format '<number> min', eg: 127 min"
YEAR_ERR_MSG = "Movie must be at leat from the year 1900"

class MovieSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'title',
            'director',
            'genre',
            'runtime',
            'release_year'
        ]
    
    title = ma.String(required=True, validate=validate.Length(min=1, max=60))
    director = ma.String(required=True, validate=validate.Length(min=1, max=50))
    genre = ma.String(required=True, validate=validate.OneOf(VALID_GENRES))
    runtime = ma.String(required=True, validate=validate.Regexp(r'^\d+\smin$'), error=RUNTIME_ERR_MSG)
    release_year = ma.Integer(required=True, validate=validate.Range(min=1900), error=YEAR_ERR_MSG)

    @pre_load
    def trim_inputs(self, data, **kwargs):
        trimmed_data = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in data.items()
        }
        return trimmed_data


# Singular movie schema instance for retreiving a single movie
movie_schema = MovieSchema()
# Multiple movies schema instance for retreiving multiple movies
movies_schema = MovieSchema(many=True)


class WatchlistMovieSchema(ma.Schema):
    # id = fields.Int()
    # title = fields.Str()
    # director = fields.Str()
    # genre = fields.Str()
    # runtime = fields.Str()
    # release_year = fields.Int()
    date_added = fields.Date()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_added')


watchlist_movie_schema = WatchlistMovieSchema()
watchlist_movies_schema = WatchlistMovieSchema(many=True)


class MovieLogMovieSchema(ma.Schema):
    # TESTING: To see if it works without specifying class variables like the watchlistmovieschema
    date_logged = fields.Date()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_logged')


movielog_movie_schema = MovieLogMovieSchema()
movielog_movies_schema = MovieLogMovieSchema(many=True)
