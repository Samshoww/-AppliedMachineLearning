# score.py
import joblib
from typing import Tuple

# Load the *entire* pipeline (vectorizer + classifier)
PIPELINE_PATH = "models/pipeline_SVM.joblib"
pipeline = joblib.load(PIPELINE_PATH)

def score(text: str, threshold: float) -> Tuple[bool, float]:
    """
    1) Calls pipeline.predict_proba on [text]
    2) Returns (prediction, propensity)
    """
    proba = pipeline.predict_proba([text])[0][1]  # P(spam)
    pred = proba >= threshold
    return bool(pred), float(proba)
