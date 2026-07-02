from flask import Blueprint, jsonify

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")

@api_v1_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API está funcionando"}), 200
