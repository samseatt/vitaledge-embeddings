# File: vitaledge-embeddings/tests/test_routes.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_embeddings_local():
    response = client.post(
        "/embeddings/generate",
        json={"texts": ["Hello world!"], "backend": "local"}
    )
    assert response.status_code == 200
    assert "embeddings" in response.json()
    assert len(response.json()["embeddings"]) == 1

def test_set_backend():
    response = client.post("/admin/set_backend", json={"backend": "openai"})
    assert response.status_code == 200
    assert response.json()["message"] == "Backend switched to openai"
