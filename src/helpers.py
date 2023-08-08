from flask import jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from models.user import User


def authenticate_user(error_msg):
    '''Decorator for authenticating users, custom error_msg can be passed in unqiuely for each endpoint'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Using verify_jwt_in_request, instead of jwt_required to minimise decorators
            verify_jwt_in_request()

            # Get the ID of the authenticated user
            authenticated_user_id = get_jwt_identity()
            # Get the user_id from the route URL
            user_id = kwargs.get('user_id')

            # Check if the authenticated user's ID matches the user_id from the URL
            if str(user_id) != authenticated_user_id:
                return jsonify(error=error_msg), 401

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def check_user_exists(f):
    '''Decorator for checking if a user exists in the DB'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the user_id from the route URL
        user_id = kwargs.get('user_id')
        # Queries user instance from DB based on ID
        user = User.query.get(user_id)
        # Return response message if user cannot be found
        if not user:
            return jsonify(error=f"User with ID of {user_id} cannot be found, please try again"), 404
        return f(*args, **kwargs)

    return decorated_function
