import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import app

client = TestClient(app)

class TestMathEndpoints(unittest.TestCase):

    def test_generate_math_problem_basic_algebra(self):
        response = client.get("/basic_algebra")
        self.assertEqual(response.status_code, 200)
        self.assertIn("problem", response.json())
        self.assertIn("solution", response.json())

    def test_generate_math_problem_addition(self):
        response = client.get("/addition")
        self.assertEqual(response.status_code, 200)
        self.assertIn("problem", response.json())
        self.assertIn("solution", response.json())

if __name__ == '__main__':
    unittest.main()
