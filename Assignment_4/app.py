# app.py
from flask import Flask, request, jsonify
import joblib
from score import score

app = Flask(__name__)

# Load the full pipeline you saved earlier
PIPELINE_PATH = "models/pipeline_SVM.joblib"
pipeline = joblib.load(PIPELINE_PATH)
THRESHOLD = 0.5

@app.route("/score", methods=["POST"])
def score_endpoint():
    data = request.get_json(force=True)
    text = data.get("text", "")
    # Use the pipeline directly inside score()
    pred, prop = score(text, THRESHOLD)
    return jsonify(prediction=int(pred), propensity=prop)

if __name__ == "__main__":
    # Listen on all interfaces so Docker port-mapping works
    app.run(host="0.0.0.0", port=5000)

