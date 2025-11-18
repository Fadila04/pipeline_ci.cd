from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_root():
    """Vérifie que GET/ retour le OK"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status" : "OK"}


def test_predict():
    """Vérifie que POST /predict retourne une prediction"""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

