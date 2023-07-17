from flask import Blueprint, jsonify
from models.watchlist import Watchlist
from schemas.watchlist_schema import watchlist_schema

# Initialises flask blueprint with a /watchlists url prefix
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
def get_watchlists(user_id):
    '''GET endpoint/handler for fetching specified users watchlist available in the cinematica app'''
    # Query all watchlist instances from the DB
    watchlists = Watchlist.query.filter_by(user_id=user_id)
    # Serialises queried watchlist instances from DB with marshmallow schema into Python DST
    result = watchlist_schema.dump(watchlists)
    # Returns the serialised data into JSON format for response
    return jsonify(result)
