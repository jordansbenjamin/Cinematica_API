from main import ma
from marshmallow import pre_load
from marshmallow.validate import Length
from schemas.movie_schema import minimal_movie_schema

TXT_ERR_MSG = "Review text must be between 5 and 2000 characters, roughly around 400 words maximum"

class ReviewSchema(ma.Schema):
    # Nesting MovieSchema in ReviewSchema
    movie = ma.Nested(minimal_movie_schema)

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
        load_only = ["id"]

    review_text = ma.String(required=True, validate=Length(min=5, max=2000, error=TXT_ERR_MSG))
    review_date = ma.Date(format="%d-%m-%Y")

    @pre_load
    def trim_inputs(self, data, **kwargs):
        '''Custom method for trimming/stripping whitespaces'''
        trimmed_data = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in data.items()
        }
        return trimmed_data

# Singular review schema instance for retreiving a single review
review_schema = ReviewSchema()
# Multiple reviews schema instance for retreiving multiple reviews
reviews_schema = ReviewSchema(many=True)
