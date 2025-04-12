import joblib
from sklearn.pipeline import Pipeline

def score(text: str, model: Pipeline, threshold: float) -> tuple[bool, float]:
    """
    Scores text using a trained model pipeline.
    Args:
        text: Input string to classify
        model: sklearn Pipeline containing TF-IDF and classifier
        threshold: Decision threshold (0-1)
    Returns:
        tuple: (prediction: bool, propensity: float)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    X = model.named_steps['tfidf'].transform([text])
    propensity = model.predict_proba(X)[0, 1]
    prediction = propensity > threshold
    
    return bool(prediction), float(propensity)