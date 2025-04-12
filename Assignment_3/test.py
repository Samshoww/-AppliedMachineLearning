import pytest
import os
import time
import requests
import joblib
from score import score

# Fixture to load model once for all tests
@pytest.fixture
def model():
    return joblib.load("models/best_model.joblib")

# Unit Tests
def test_score(model):
    """Tests all requirements from assignment"""
    # Smoke test
    text = "Free money now!"
    prediction, propensity = score(text, model, 0.5)
    
    # Format tests
    assert isinstance(prediction, bool)
    assert isinstance(propensity, float)
    assert 0 <= propensity <= 1
    
    # Threshold tests
    assert score(text, model, 0.0)[0] == True
    assert score(text, model, 1.0)[0] == False
    
    # Obvious cases
    assert score("Win a free iPhone!", model, 0.5)[0] == True
    assert score("Hello, how are you?", model, 0.5)[0] == False

# Integration Test
def test_flask():
    """Tests Flask endpoint lifecycle"""
    # Launch Flask
    flask_process = os.popen("python app.py")
    time.sleep(3)  # Wait for startup
    
    try:
        # Test endpoint
        response = requests.post(
            'http://localhost:5000/score',
            json={'text': 'Free credit card'},
            timeout=5
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data['prediction'], bool)
        assert 0 <= data['propensity'] <= 1
    finally:
        # Kill Flask
        os.system("taskkill /f /im python.exe")