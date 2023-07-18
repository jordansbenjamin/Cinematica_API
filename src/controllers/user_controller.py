from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from models.user import User
from schemas.user_schema import user_schema, users_schema
from controllers.watchlist_controller import watchlists_bp
from controllers.movielog_controller import movielogs_bp
from controllers.review_controller import reviews_bp
from controllers.rating_controller import ratings_bp

# Initialises flask blueprint with a /users url prefix
users_bp = Blueprint('users', __name__, url_prefix="/users")

# Nesting users blueprint prefix endpoint with other bp endpoints:
users_bp.register_blueprint(
    watchlists_bp, url_prefix='<int:user_id>/watchlist')
users_bp.register_blueprint(movielogs_bp, url_prefix='<int:user_id>/movielogs')
users_bp.register_blueprint(reviews_bp, url_prefix='<int:user_id>/reviews')
users_bp.register_blueprint(ratings_bp, url_prefix='<int:user_id>/ratings')


@users_bp.route("/", methods=["GET"])
def get_all_users():
    '''GET endpoint/handler for fetching all users available in the cinematica app'''
    # Queries all user instances from the DB
    users = User.query.all()
    # Serialises queried user instances from DB with marshmallow schema into Python DST
    response = users_schema.dump(users)
    # Returns the serialised data into JSON format for response
    return jsonify(response), 200


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    # Queries first instance of user filtered by ID
    user = User.query.filter_by(id=user_id).first()

    # Check if user exists
    if user:
        # Single user instance serialised
        response = user_schema.dump(user)
        # Returns user information back as JSON
        return jsonify(response), 200
    else:
        return abort(404, description="User does not exist")
        # NOTE: This does the same thing, I'll keep it here for reference
        # return jsonify(message="User does not exist, please try again"), 404


@users_bp.route("/", methods=["POST"])
def create_user():
    # NOTE: Use exception handling to validate the fields loaded from the request body is provided
    user_body_data = user_schema.load(request.json)
    # Queries existing email from user_body_data email field
    existing_email = User.query.filter_by(
        email=user_body_data["email"]).first()
    # Queries existing email from user_body_data email field
    existing_username = User.query.filter_by(
        username=user_body_data["username"]).first()

    # Checks if a user's email is registered
    if existing_email:
        return abort(409, description="Email already registered, please try again.")
    # Checks if a user's username is registered    
    elif existing_username:
        return abort(409, description="Username already registered, please try again.")

    # Creates new user instance
    new_user = User(
        email=user_body_data.get("email"),
        username=user_body_data.get("username"),
        password=bcrypt.generate_password_hash(user_body_data.get("password"))
    )

    # Add new user instance to db and commit
    db.session.add(new_user)
    db.session.commit()
    # Returns new user information as a JSON respone
    response = user_schema.dump(new_user)
    return jsonify(response), 201