from flask import Blueprint, jsonify, request
from main import bcrypt
from marshmallow.exceptions import ValidationError
from models.user import User
from schemas.user_schema import auth_user_schema
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def auth_login():
    '''POST route for logging in user based on username and password, presenting their token for accessing certain endpoints'''
    # Validating user request body data with schema
    try:
        # If successful, load the request body data
        user_body_data = auth_user_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Query user from DB filtered by username
    user = User.query.filter_by(username=user_body_data["username"]).first()

    # Checks if the user exists and the password matches
    if user and bcrypt.check_password_hash(user.password, user_body_data["password"]):
        # Create the access token required for logging in
        token = create_access_token(identity=str(
            user.id), expires_delta=timedelta(days=1))
        # Return successful response along with the token and expiry
        return jsonify(message="Successfully logged in!", username=user.username, token=token, expiry="24 hrs"), 200
    else:
        # If username and password doesn't match return error
        return jsonify(message="Invalid username and password, please try again"), 401
