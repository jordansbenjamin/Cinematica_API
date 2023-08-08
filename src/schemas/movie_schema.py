from main import ma
from marshmallow import fields, validates, pre_load
from marshmallow.validate import Length
from marshmallow.exceptions import ValidationError
import re

VALID_GENRES = ('Drama', 'Action', 'Comedy', 'Sci-fi', 'Thriller', 'Superhero', 'Romance', 'Horror', 'Adventure', 'Animation',
                'Fantasy', 'Musical', 'Mystery', 'Family', 'Crime', 'Documentary', 'Western', 'Biographical', 'War', 'Film-Noir', 'Rom-Com')
RUNTIME_ERR_MSG = "Runtime must be in the format '<number> min', eg: 127 min"
YEAR_ERR_MSG = "Movie must be at least from the year 1900"


class MovieSchema(ma.Schema):
    # modifying id attribute for changing id field name
    movie_id = ma.Integer(attribute="id")

    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'movie_id',
            'title',
            'director',
            'genre',
            'runtime',
            'release_year'
        ]

    title = ma.String(required=True, error_messages={
                      "required": "Title is required."}, validate=Length(min=1, max=60))
    director = ma.String(required=True, error_messages={
                         "required": "Director is required."}, validate=Length(min=1, max=50))
    genre = ma.String(required=True, error_messages={
                      "required": "Genre is required."})
    runtime = ma.String(required=True, error_messages={
                        "required": "Runtime is required."})
    release_year = ma.Integer(required=True, error_messages={
                              "required": "Release year is required."})

    @validates('genre')
    def validate_genres(self, value):
        '''Custom method for validating genre input'''
        # Check if value contains any characters other than letters, spaces, and forward slashes
        if re.search('[^a-zA-Z\s/-]', value):
            raise ValidationError(
                "Genres must be separated by forward slashes and contain only letters.")

        # Splitting by forward slash
        genres = value.split('/')

        # Check if at least one genre is present
        if not genres:
            raise ValidationError("At least one genre must be provided.")

        # Validate that each genre is a known genre
        for genre in genres:
            genre = genre.strip()  # Remove any leading/trailing spaces
            if genre not in VALID_GENRES:
                raise ValidationError(f"Genre '{genre}' is not a valid genre.")

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
        '''Custom method for trimming/stripping whitespaces'''
        trimmed_data = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in data.items()
        }
        return trimmed_data


# Singular movie schema instance for retreiving a single movie
movie_schema = MovieSchema()
# Multiple movies schema instance for retreiving multiple movies
movies_schema = MovieSchema(many=True)

# Fields to exclude for minimal movie schema instance
movie_fields_to_exclude = ['director', 'genre', 'runtime', 'release_year']

# Minimal instance of the MovieSchema, excluding the unwanted fields
minimal_movie_schema = MovieSchema(exclude=movie_fields_to_exclude)


class UpdateMovieSchema(ma.Schema):
    # modifying id attribute for changing id field name
    movie_id = ma.Integer(attribute="id")

    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'movie_id',
            'title',
            'director',
            'genre',
            'runtime',
            'release_year'
        ]

    title = ma.String(validate=Length(min=1, max=60))
    director = ma.String(validate=Length(min=1, max=50))
    genre = ma.String()
    runtime = ma.String()
    release_year = ma.Integer()

    @validates('genre')
    def validate_genres(self, value):
        '''Custom method for validating genre input'''
        # Check if value contains any characters other than letters, spaces, and forward slashes
        if re.search('[^a-zA-Z\s/-]', value):
            raise ValidationError(
                "Genres must be separated by forward slashes and contain only letters.")

        # Splitting by forward slash
        genres = value.split('/')

        # Check if at least one genre is present
        if not genres:
            raise ValidationError("At least one genre must be provided.")

        # Validate that each genre is a known genre
        for genre in genres:
            genre = genre.strip()  # Remove any leading/trailing spaces
            if genre not in VALID_GENRES:
                raise ValidationError(f"Genre '{genre}' is not a valid genre.")

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
        '''Custom method for trimming/stripping whitespaces'''
        trimmed_data = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in data.items()
        }
        return trimmed_data


# Singular movie schema instance for retreiving a single movie
update_movie_schema = UpdateMovieSchema()


class WatchlistMovieSchema(ma.Schema):
    # modifying id attribute for changing id field name
    movie_id = ma.Integer(attribute="id")
    # adding date_added field for each movie added into watchlist
    date_added = fields.Date(format="%d-%m-%Y")

    class Meta:
        ordered = True
        fields = ('movie_id', 'title')


# Singular watchlist movie schema instance for retreiving nested movie information into a users watchlist
watchlist_movie_schema = WatchlistMovieSchema()


class MovieLogMovieSchema(ma.Schema):
    # modifying id attribute for changing id field name
    movie_id = ma.Integer(attribute="id")
    # adding date_logged field for each movie logged into the movielog
    date_logged = fields.Date()

    class Meta:
        ordered = True
        fields = ('movie_id', 'title', 'director', 'genre',
                  'runtime', 'release_year', 'date_logged')


# Singular movielog movie schema instance for retreiving nested movie information into a users movielog
movielog_movie_schema = MovieLogMovieSchema()
