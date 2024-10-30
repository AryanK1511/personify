from app import app
from flask import jsonify, request


@app.route("/submit-url", methods=["POST"])
def receive_url():
    data = request.get_json()
    url = data.get("url")

    return jsonify({"message": f"URL received: {url}"}), 200
