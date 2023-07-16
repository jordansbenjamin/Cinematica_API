from main import ma


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