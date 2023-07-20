from main import ma
from marshmallow import post_dump
from schemas.movie_schema import MovieSchema

class RatingSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'rating_score',
            'rating_date',
            'movie'
        ]
    movie = ma.Nested(MovieSchema)

    # post_dump decorator will call the format rating func after schema dumps the data
    @post_dump
    # Self refers to instance of the schema, data is the serialised data that RatingSchema created
    def format_rating(self, data, **kwargs):
        '''Modify the rating_score to be a string in the format "5/5"'''
        data['rating_score'] = f"{data['rating_score']}/5"
        return data
    

# Singular rating schema instance for retreiving a single rating
rating_schema = RatingSchema()
# Multiple ratings schema instance for retreiving multiple ratings
ratings_schema = RatingSchema(many=True)