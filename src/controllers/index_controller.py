from flask import Blueprint, jsonify

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    return jsonify(message="Welcome to Cinematica! A RESTful API for movie enthusiasts to keep track and share their cinematic journey!")