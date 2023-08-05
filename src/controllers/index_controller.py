from flask import Blueprint, jsonify

# Initialises flask blueprint
index_bp = Blueprint('index', __name__)


@index_bp.route("/")
def index():
    return jsonify(message="Welcome to Cinematica! For movie enthusiasts to keep track and share their cinematic journey!")
