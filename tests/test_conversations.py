from fastapi.testclient import TestClient
from app.main import app


def test_create_conversation():
    with TestClient(app) as client:
        response = client.post("/conversations", json={"name": "Test", "model": "gpt-4o-mini"})
        print(response.text)
        assert response.status_code == 201
        assert "id" in response.json()
