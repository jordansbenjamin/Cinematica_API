from main import ma


class MovieLogSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'log_date',
        ]

# Singular movie_log schema instance for retreiving a single movie_log
movielog_schema = MovieLogSchema()
# COMMENTED OUT BECAUSE TECHNICALLY A USER ONLY HAS ONE MOVIELOG
# WILL DELETE IN THE FUTURE, KEEPING IT JUST IN CASE
# # Multiple movie_logs schema instance for retreiving multiple movie_logs
# movie_logs_schema = MovieLogSchema(many=True)