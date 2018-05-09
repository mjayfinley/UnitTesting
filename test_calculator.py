import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(4,4)

    def test_add(self):
        result = self.calculator.add()
        self.assertEqual(8,result)

    def test_subtract(self):
        result = self.calculator.subtract()
        self.assertEqual(0,result)

    def test_multiply(self):
        result = self.calculator.multiply()
        self.assertEqual(16,result)

    def test_divide(self):
        result = self.calculator.divide()
        self.assertEqual(1,result)

if __name__ == '__main__':
    unittest.main()
