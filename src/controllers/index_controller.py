from flask import Blueprint, jsonify

# Initialises flask blueprint
index_bp = Blueprint('index', __name__)


@index_bp.route("/")
def index():
    '''Index endpoint for displaying a welcome message to users'''
    
    return jsonify(message="Welcome to Cinematica! A web API for movie enthusiasts to keep track and share their thoughts whilst embarking on their cinematic journey!")
