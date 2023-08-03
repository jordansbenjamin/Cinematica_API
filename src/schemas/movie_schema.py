from main import ma
from marshmallow import fields, validates, pre_load
from marshmallow.validate import Length, OneOf
from marshmallow.exceptions import ValidationError
import re

VALID_GENRES = ('Drama', 'Action', 'Comedy', 'Sci-fi', 'Thriller', 'Superhero', 'Romance', 'Horror', 'Adventure', 'Animation', 'Fantasy', 'Musical', 'Mystery', 'Family', 'Crime', 'Documentary', 'Western', 'Biographical', 'War', 'Film-noir')
RUNTIME_ERR_MSG = "Runtime must be in the format '<number> min', eg: 127 min"
YEAR_ERR_MSG = "Movie must be at least from the year 1900"

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
    
    title = ma.String(required=True, validate=Length(min=1, max=60))
    director = ma.String(required=True, validate=Length(min=1, max=50))
    genre = ma.String(required=True, validate=OneOf(VALID_GENRES))
    runtime = ma.String(required=True)
    release_year = ma.Integer(required=True)

    @validates('runtime')
    def validate_runtime(self, value):
        '''Custom method for validating runtime using Regex'''
        if not re.match(r'^\d+\smin$', value):
            raise ValidationError(RUNTIME_ERR_MSG)
        
    @validates('release_year')
    def validate_release_year(self, value):
        '''Custom method for validating release year based on year range'''
        if value <= 1900:
            raise ValidationError(YEAR_ERR_MSG)

    @pre_load
    def trim_inputs(self, data, **kwargs):
        '''Custome method for trimming/stripping whitespaces'''
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
    date_added = fields.Date()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_added')


watchlist_movie_schema = WatchlistMovieSchema()


class MovieLogMovieSchema(ma.Schema):
    date_logged = fields.Date()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_logged')


movielog_movie_schema = MovieLogMovieSchema()
