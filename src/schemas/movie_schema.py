from main import ma
from marshmallow import fields


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


# Singular movie schema instance for retreiving a single movie
movie_schema = MovieSchema()
# Multiple movies schema instance for retreiving multiple movies
movies_schema = MovieSchema(many=True)


class WatchlistMovieSchema(ma.Schema):
    id = fields.Int()
    title = fields.Str()
    director = fields.Str()
    genre = fields.Str()
    runtime = fields.Str()
    release_year = fields.Int()
    date_added = fields.DateTime()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_added')


watchlist_movie_schema = WatchlistMovieSchema()
watchlist_movies_schema = WatchlistMovieSchema(many=True)


class MovieLogMovieSchema(ma.Schema):
    # TESTING: To see if it works without specifying class variables like the watchlistmovieschema
    date_logged = fields.DateTime()

    class Meta:
        ordered = True
        fields = ('id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_logged')


movielog_movie_schema = MovieLogMovieSchema()
movielog_movies_schema = MovieLogMovieSchema(many=True)
