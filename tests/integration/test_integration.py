import pytest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import app

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

def test_basic_algebra_endpoint(test_client):
    response = test_client.get("/basic_algebra")
    assert response.status_code == 200
    assert "problem" in response.json()
    assert "solution" in response.json()

def test_addition_endpoint(test_client):
    response = test_client.get("/addition")
    assert response.status_code == 200
    assert "problem" in response.json()
    assert "solution" in response.json()
