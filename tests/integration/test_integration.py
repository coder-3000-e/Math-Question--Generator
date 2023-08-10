import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.integration
def test_basic_algebra_endpoint():
    response = client.get("/basic_algebra")
    assert response.status_code == 200
    assert "problem" in response.json()
    assert "solution" in response.json()

@pytest.mark.integration
def test_addition_endpoint():
    response = client.get("/addition")
    assert response.status_code == 200
    assert "problem" in response.json()
    assert "solution" in response.json()
