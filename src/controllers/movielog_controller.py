from flask import Blueprint, jsonify
from models.movielog import MovieLog
from schemas.movielog_schema import movielog_schema

# Initialises flask blueprint for movielogs, prefix is nested and registered with users bp
movielogs_bp = Blueprint('movielogs', __name__)


@movielogs_bp.route("/", methods=["GET"])
def get_movielogs(user_id):
    '''GET endpoint/handler for fetching specified users movielog available in the cinematica app'''
    # Queries movielog instance from the DB
    movielog = MovieLog.query.filter_by(user_id=user_id).first()
    # Serialises queried movielog instance from DB with marshmallow schema into Python DST
    result = movielog_schema.dump(movielog)
    # Returns the serialised data into JSON format for response
    return jsonify(result)