from flask import Blueprint, jsonify
from models.user import User
from schemas.user_schema import user_schema, users_schema
from watchlist_controller import watchlists_bp
from movielog_controller import movielogs_bp
from review_controller import reviews_bp

# Initialises flask blueprint with a /users url prefix
users_bp = Blueprint('users', __name__, url_prefix="/users")
# Nesting users blueprint prefix endpoint with other bp endpoints:
users_bp.register_blueprint(watchlists_bp, url_prefix='<int:user_id>/watchlist')
users_bp.register_blueprint(movielogs_bp, url_prefix='<int:user_id>/movielogs')
users_bp.register_blueprint(reviews_bp, url_prefix='<int:user_id>/reviews')

@users_bp.route("/", methods=["GET"])
def get_users():
    '''GET endpoint/handler for fetching all users available in the cinematica app'''
    # Query all user instances from the DB
    users = User.query.all()
    # Serialises queried user instances from DB with marshmallow schema into Python DST
    result = users_schema.dump(users)
    # Returns the serialised data into JSON format for response
    return jsonify(result)
