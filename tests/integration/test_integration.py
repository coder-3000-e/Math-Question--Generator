import pytest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
