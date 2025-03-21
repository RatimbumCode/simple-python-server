from flask import Flask, jsonify, request
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
VERIFICATION_TOKEN = os.environ.get("API_TOKEN")
if not VERIFICATION_TOKEN:
    raise ValueError("API_TOKEN environment variable must be set")


@app.route("/", methods=["GET"])
def hello():
    # Get token from query parameter (e.g., ?token=my-secret-token-123)
    provided_token = request.args.get("token")

    # Verify token
    if not provided_token or provided_token != VERIFICATION_TOKEN:
        return (
            jsonify(
                {
                    "message": "Invalid or missing verification token.",
                    "status": "error",
                    "timestamp": datetime.datetime.now().isoformat(),
                }
            ),
            401,
        )  # Unauthorized status code

    # If token is valid, return the success response
    response_data = {
        "message": "Hello! This is a JSON response from Flask.",
        "status": "success",
        "timestamp": datetime.datetime.now().isoformat(),
        "method": "GET",
        "path": "/",
    }
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
