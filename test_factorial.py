import unittest
from factorial import Factorial

class TestFactorial(unittest.TestCase):

    def setUp(self):
        self.factorial = Factorial(5)

    def test_calc_factorial(self):
        result = self.factorial.calc_factorial()
        self.assertEqual(120,result)

if __name__ == '__main__':
    unittest.main()
