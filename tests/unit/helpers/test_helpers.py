import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.helpers.helpers import remove_dollar_sign

class TestRemoveDollarSign(unittest.TestCase):

    def test_remove_dollar_sign(self):
        input_string = "$100"
        expected_output = "100"
        result = remove_dollar_sign(input_string)
        self.assertEqual(result, expected_output)

    def test_no_dollar_sign(self):
        input_string = "200"
        expected_output = "200"
        result = remove_dollar_sign(input_string)
        self.assertEqual(result, expected_output)

    def test_empty_string(self):
        input_string = ""
        expected_output = ""
        result = remove_dollar_sign(input_string)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
