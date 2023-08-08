from main import ma
from marshmallow.validate import Length, Regexp, Email

EMAIL_ERR_MSG = "Email address provided does not have the correct format"
USERNAME_ERR_MSG = "Username must be between 3 to 25 characters"
USERNAME_REGX_ERR_MSG = "Only letters, underscores and numbers are allowed for usernames"
PW_ERR_MSG = "Password must be between 6 to 25 characters"
PW_REGX_ERR_MSG = "Password cannot contain whitespaces"


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

    # Formatting join_date
    join_date = ma.Date(format="%d-%m-%Y")

    # Validating email
    email = ma.String(
        required=True, error_messages={"required": "Email is required."},  validate=Email(error=EMAIL_ERR_MSG))

    # Validating username length and characters with regex
    username = ma.String(required=True, error_messages={"required": "Username is required."}, validate=[Length(
        min=3, max=25, error=USERNAME_ERR_MSG), Regexp(r'^[a-zA-Z0-9_]+$', error=USERNAME_REGX_ERR_MSG)])

    # Validating password length and characters with regex
    password = ma.String(required=True, error_messages={"required": "Password is required."}, validate=[Length(
        min=6, max=25, error=PW_ERR_MSG), Regexp(r'^\S*$', error=PW_REGX_ERR_MSG)])


# Singular user schema instance for retreiving a single user
user_schema = UserSchema()
# Multiple users schema instance for retreiving multiple users
users_schema = UserSchema(many=True)


class UpdateUserSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'email',
            'username',
            'password',
        ]
        load_only = ["password"]

    # Validating email
    email = ma.String(validate=Email(error=EMAIL_ERR_MSG))

    # Validating username length and characters with regex
    username = ma.String(validate=[Length(min=3, max=25, error=USERNAME_ERR_MSG), Regexp(
        r'^[a-zA-Z0-9_]+$', error=USERNAME_REGX_ERR_MSG)])

    # Validating password length and characters with regex
    password = ma.String(validate=[Length(
        min=6, max=25, error=PW_ERR_MSG), Regexp(r'^\S*$', error=PW_REGX_ERR_MSG)])


# Singular user schema instance for retreiving a single user
update_user_schema = UpdateUserSchema()


class AuthUserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = [
            'username',
            'password'
        ]

    # Validating username length and characters with regex
    username = ma.String(required=True, error_messages={"required": "Username is required."}, validate=[Length(
        min=3, max=25, error=USERNAME_ERR_MSG), Regexp(r'^[a-zA-Z0-9_]+$', error=USERNAME_REGX_ERR_MSG)])

    # Validating password length and characters with regex
    password = ma.String(required=True, error_messages={"required": "Password is required."}, validate=[Length(
        min=6, max=25, error=PW_ERR_MSG), Regexp(r'^\S*$', error=PW_REGX_ERR_MSG)])


auth_user_schema = AuthUserSchema()
