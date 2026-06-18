from flask import Flask, render_template, request, jsonify

from scanner.scan_engine import run
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../frontend"),
    style_folder=os.path.join(BASE_DIR, "../frontend/style")
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scanner", methods=["POST"])
def scan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    target = data.get("target")
    profile = data.get("profiles")

    if not target or not profile:
        return jsonify({"error": "Missing target or profile"}), 400

    try:
        results = run(profile, target)
        return jsonify(results), 200

    except Exception as e:
        return jsonify({
            "error": "Scan failed",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)