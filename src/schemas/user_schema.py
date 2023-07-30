from main import ma
from marshmallow import validate

email_error_msg = "Email address provided does not have the correct format"
username_error_msg = "Username must be between 3 to 25 characters"
username_regx_error_msg = "Only letters, underscores and numbers are allowed for usernames"
pw_error_msg = "Password must be between 6 to 25 characters"
pw_regx_error_msg = "Password cannot contain whitespaces"


class UserSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'email',
            'username',
            'password',
            'join_date'
        ]
        load_only = ["email", "password"]

    # Validating email
    email = ma.String(
        required=True, error_messages={"required": "Email is required."},  validate=validate.Email(error=email_error_msg))

    # Validating username length and characters with regex
    username = ma.String(required=True, error_messages={"required": "Username is required."}, validate=[validate.Length(
        min=3, max=25, error=username_error_msg), validate.Regexp(r'^[a-zA-Z0-9_]+$', error=username_regx_error_msg)])

    # Validating password length and characters with regex
    password = ma.String(required=True, error_messages={"required": "Password is required."}, validate=[validate.Length(
        min=6, max=25, error=pw_error_msg), validate.Regexp(r'^\S*$', error=pw_regx_error_msg)])


# Singular user schema instance for retreiving a single user
user_schema = UserSchema()
# Multiple users schema instance for retreiving multiple users
users_schema = UserSchema(many=True)
