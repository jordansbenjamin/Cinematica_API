from flask import Blueprint, jsonify, request
from main import db, bcrypt
from marshmallow.exceptions import ValidationError
from models.user import User
from schemas.user_schema import user_schema
from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def auth_login():

    # Validating user request body data with schema
    try:
        # If successful, load the request body data
        user_body_data = user_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    user = User.query.filter_by(username=user_body_data["username"]).first()

    if user and bcrypt.check_password_hash(user.password, user_body_data["password"]):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return jsonify(username=user.username, token=token, expiry="24hrs")
    else:
        return jsonify(message="Invalid username and password, please try again"), 401