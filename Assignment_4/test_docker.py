# test_docker.py

import subprocess
import time
import requests

def test_docker_endpoint():
    # 1) Build the image (force rebuild so CI always uses latest)
    subprocess.run(["docker", "build", "-t", "spam-svc", "."], check=True)

    # 2) Run the container
    proc = subprocess.Popen([
        "docker", "run", "--rm", "-d",
        "-p", "5000:5000",
        "--name", "spam-svc-test",
        "spam-svc"
    ])
    time.sleep(3)  # wait for the app to start

    try:
        # 3) Hit the /score endpoint
        r = requests.post(
            "http://127.0.0.1:5000/score",
            json={"text":"Containerization test"}
        )
        assert r.status_code == 200
        data = r.json()
        assert set(data) == {"prediction", "propensity"}
    finally:
        # 4) Tear down the container
        subprocess.run(["docker", "rm", "-f", "spam-svc-test"], check=True)
