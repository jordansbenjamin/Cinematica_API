from main import ma


class RatingSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'rating_score',
            'rating_date'
        ]

# Singular rating schema instance for retreiving a single rating
rating_schema = RatingSchema()
# Multiple ratings schema instance for retreiving multiple ratings
ratings_schema = RatingSchema(many=True)