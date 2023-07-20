from main import ma
from schemas.movie_schema import MovieSchema

class ReviewSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'review_text',
            'review_date',
            'movie'
        ]
    movie = ma.Nested(MovieSchema)

# Singular review schema instance for retreiving a single review
review_schema = ReviewSchema()
# Multiple reviews schema instance for retreiving multiple reviews
reviews_schema = ReviewSchema(many=True)