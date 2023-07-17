from flask import Blueprint, jsonify
from models.watchlist import Watchlist
from schemas.watchlist_schema import watchlist_schema

# Initialises flask blueprint for watchlists, prefix is nested and registered with users bp
watchlists_bp = Blueprint('watchlists', __name__)


@watchlists_bp.route("/", methods=["GET"])
def get_watchlists(user_id):
    '''GET endpoint/handler for fetching specified users watchlist available in the cinematica app'''
    # Queries watchlist instance from the DB
    watchlist = Watchlist.query.filter_by(user_id=user_id).first()
    # Serialises queried watchlist instance from DB with marshmallow schema into Python DST
    result = watchlist_schema.dump(watchlist)
    # Returns the serialised data into JSON format for response
    return jsonify(result)
