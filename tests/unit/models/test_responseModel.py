import unittest
from pydantic import ValidationError
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.models.responseModel import MathProblemResponse

class TestMathProblemResponse(unittest.TestCase):

    def test_valid_math_problem_response(self):
        problem = "2 + 2"
        solution = "4"
        response = MathProblemResponse(problem=problem, solution=solution)
        self.assertEqual(response.problem, problem)
        self.assertEqual(response.solution, solution)

    def test_missing_fields(self):
        with self.assertRaises(ValidationError):
            MathProblemResponse()

    def test_invalid_types(self):
        with self.assertRaises(ValidationError):
            MathProblemResponse(problem=42, solution="four")

if __name__ == '__main__':
    unittest.main()
