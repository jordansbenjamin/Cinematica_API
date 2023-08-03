from main import ma
from marshmallow import fields
from schemas.movie_schema import MovieLogMovieSchema

class MovieLogSchema(ma.Schema):
    # modifying id attribute for changing id field name
    movielog_id = ma.Integer(attribute="id")
    # Nesting MovielogMovieSchema to add movies under MovielogSchema
    movies = ma.Nested(MovieLogMovieSchema, many=True, attribute="movies")
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'movielog_id',
            'movies',
        ]

# Singular movie_log schema instance for retreiving a single movie_log
movielog_schema = MovieLogSchema()
