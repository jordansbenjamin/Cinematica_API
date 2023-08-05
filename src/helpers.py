from flask import jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def authenticate_user(error_message):
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
                return jsonify(message=error_message), 401

            return f(*args, **kwargs)

        return decorated_function

    return decorator