"""
app.py
------
Flask web application (GUI) for the Email Spam Detection project.

Loads the trained TF-IDF + Naive Bayes model and serves a user-friendly
web interface where a user can paste an email/message and instantly see
whether it is classified as SPAM or NOT SPAM, along with a confidence score.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import os
import re
import traceback

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

print("Loading model and vectorizer...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print("Model loaded successfully. Ready to serve requests.")


def clean_text(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True) or {}
        message = clean_text(data.get("message", ""))

        if not message:
            return jsonify({"error": "Please enter a message to check."}), 400

        vec = vectorizer.transform([message])
        prediction = model.predict(vec)[0]
        probabilities = model.predict_proba(vec)[0]  # [ham_prob, spam_prob]

        ham_prob = round(float(probabilities[0]) * 100, 2)
        spam_prob = round(float(probabilities[1]) * 100, 2)

        result = {
            "label": "spam" if prediction == 1 else "ham",
            "spam_probability": spam_prob,
            "ham_probability": ham_prob,
            "confidence": max(spam_prob, ham_prob),
        }
        return jsonify(result)

    except Exception as e:
        # Print the full traceback to the terminal so it's easy to debug,
        # and always return valid JSON (never an empty body) to the browser.
        traceback.print_exc()
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error. Check the terminal for details."}), 500


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
