from main import ma
from marshmallow import fields, validate

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
    genre = ma.String(required=True, validate=validate.Length(max=50))
    runtime = ma.String(required=True, validate=validate.Regexp(r'^\d+\smin$'))
    release_year = ma.Integer(required=True, validate=validate.Range(min=1899))


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
