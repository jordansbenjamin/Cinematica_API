from flask import Blueprint, jsonify, request, abort
from marshmallow.exceptions import ValidationError
from main import db, bcrypt
from models.user import User
from models.watchlist import Watchlist
from models.movielog import MovieLog
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
users_bp.register_blueprint(movielogs_bp, url_prefix='<int:user_id>/movielog')
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
    '''GET endpoint/handler for fetching single user by ID'''

    # Queries first instance of user filtered by ID
    user = User.query.filter_by(id=user_id).first()

    # Check if user exists
    if user:
        # Single user instance serialised
        response = user_schema.dump(user)
        # Returns user information back as JSON
        return jsonify(response), 200
    else:
        return jsonify(message=f"User with ID of {user_id} cannot be found, please try again"), 404


@users_bp.route("/", methods=["POST"])
def create_user():
    '''POST endpoint/handler for creating/registering a new user'''

    # Validating user request body data with schema
    try:
        # If successful, load the request body data
        user_body_data = user_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # Queries existing email from user_body_data email field
    existing_email = User.query.filter_by(
        email=user_body_data["email"]).first()
    # Queries existing email from user_body_data email field
    existing_username = User.query.filter_by(
        username=user_body_data["username"]).first()

    # Checks if a user's email is registered
    if existing_email:
        return abort(409, description=f"Email of {existing_email.email} already registered, please try again")
    # Checks if a user's username is registered
    elif existing_username:
        return abort(409, description=f"Username of {existing_username.username} already registered, please try again")

    # Creates new user instance
    new_user = User(
        email=user_body_data.get("email"),
        username=user_body_data.get("username"),
        password=bcrypt.generate_password_hash(
            user_body_data.get("password")).decode("utf-8")
    )

    # Add new user instance to db
    db.session.add(new_user)
    # Commit user in order to associate watchlist and movielog
    db.session.commit()

    # Newly registered users will have a watchlist and movielog created for them automatically
    # Creates new watchlist instance for the user
    new_watchlist = Watchlist(user_id=new_user.id)
    # Creates new movielog instance for the user
    new_movielog = MovieLog(user_id=new_user.id)

    # Add new watchlist movielog instances to db and commit
    db.session.add_all([new_watchlist, new_movielog])
    db.session.commit()

    # Returns new user information as a JSON respone
    response = user_schema.dump(new_user)
    return jsonify(message="You have sucessfully registered!", new_user=response), 201


@users_bp.route("/<int:user_id>", methods=["PUT"])
# NOTE: Will add jwt_required when auth feature is added
def update_user(user_id):
    '''PUT endpoint for updating specified user'''

    # Queries user from DB
    user = User.query.filter_by(id=user_id).first()
    # Checks to see if user exists
    if not user:
        jsonify(
            message=f"User with ID of {user_id} cannot be found, please try again"), 404
    # Checks if the user_id matches
    elif user.id != user_id:
        return jsonify(message="You are not authorised to update or make changes to this user."), 401

    # Validating user request body data with schema
    try:
        # If successful, load the request body data
        user_body_data = user_schema.load(request.json)
    except ValidationError as error:
        # If fail, return error message
        return jsonify(error.messages), 400

    # User can update any fields indvidually with the aid for these functions to update user object in memory:
    def update_email(user, new_email):
        '''Updates the user email'''

        # Checks to see if the new email matches with the current email
        if user.email == new_email:
            return jsonify(message="Cannot update, new email matches with current email, please try another email."), 409

        # Queries database by filtering email to find match of user_body_data
        existing_user_email = User.query.filter_by(
            email=new_email).first()

        # If the same email already exist then return error
        if existing_user_email:
            return jsonify(message="Email is already registered."), 409
        # Else update the users registered email with the new email passed in to the body data
        else:
            user.email = new_email

    def update_username(user, new_username):
        '''Updates the username'''

        # Checks to see if the new username matches with the current username
        if user.username == new_username:
            return jsonify(message="Cannot update, new username matches with current username, please try another username."), 409

        # Queries database by filtering username to find match of user_body_data
        existing_username = User.query.filter_by(username=new_username).first()

        # If the same username already exist then return error
        if existing_username:
            return jsonify(message=f"Username of {existing_username.username} is already registered."), 409
        # Else update the users registered username with the new username passed in to the body data
        else:
            user.username = new_username

    def update_password(user, new_password):
        '''Updates the users password'''

        # Check if password exists
        if bcrypt.check_password_hash(user.password, new_password):
            # Returns error msg if it does
            return jsonify(message="Password can't be the same as current password."), 409
        else:
            # Updates the password with the new password otherwise
            user.password = bcrypt.generate_password_hash(
                new_password).decode("utf-8")

    # Mapping keys to update functions
    updates = {
        "email": update_email,
        "username": update_username,
        "password": update_password
    }

    # Loops through updates dict to call func for updating user data
    for field, update_func in updates.items():
        if field in user_body_data:
            result = update_func(user, user_body_data[field])
            if result is not None:
                return result

    db.session.commit()
    response = user_schema.dump(user)
    return jsonify(message="Account update successful!", user=response), 200


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    '''DELETE endpoint for deleting specified user'''
    # Queries user from DB
    user = User.query.filter_by(id=user_id).first()
    # Checks if the user_id matches
    if user.id != user_id:
        return jsonify(message="You are not authorised to delete this user."), 401
    # Checks if user exists
    if user:
        # Save user data before deleting
        user_data = user_schema.dump(user)
        # If user exist, then delete user instance from DB
        db.session.delete(user)
        db.session.commit()

        return jsonify(message="User sucessfully deleted!", user=user_data)
    else:
        # Responds with 404 message otherwise
        return jsonify(message=f"User of ID {user_id} not found."), 404
