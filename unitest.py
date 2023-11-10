import unittest
from num2words import num2words
from eurodreams import *

class TestFactorialConversion(unittest.TestCase):

    def test_calculate_factorial(self):
        result = calculate_factorial()
        self.assertEqual(result, 19191900) 

    def test_convert_to_words(self):
        result = convert_to_words()
        self.assertEqual(result, "nineteen million, one hundred and ninety-one thousand, nine hundred")  # Replace with the actual expected result

if __name__ == '__main__':
    unittest.main()