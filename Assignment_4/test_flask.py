# test_flask.py

import subprocess
import time
import requests

def test_flask_endpoint():
    """Integration test: launch Flask, hit /score, then tear down."""
    proc = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # give server time to start

    try:
        r = requests.post(
            "http://127.0.0.1:5000/score",
            json={"text":"Integration test text"}
        )
        assert r.status_code == 200

        data = r.json()
        # Must have both keys and valid types/ranges
        assert set(data) == {"prediction", "propensity"}
        assert data["prediction"] in (0,1)
        assert 0.0 <= data["propensity"] <= 1.0
    finally:
        proc.terminate()
        proc.wait(timeout=5)
