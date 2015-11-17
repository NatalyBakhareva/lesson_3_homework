from unittest import TestCase
from calculator import Calculator
import unittest


class CalculatorTest(TestCase):
    def setUp(self):
        self.num = Calculator()

    def test_add(self):
        self.assertEqual(self.num.add(0, 0), 0)
        self.assertEqual(self.num.add(2.5, 3), 5.5)
        self.assertEqual(self.num.add(-5, 3), -2)
        self.assertEqual(self.num.add(-10, -5), -15)
        self.assertNotEqual(self.num.add(10, -2), 12)

    def test_subtract(self):
        self.assertEqual(self.num.subtract(0, 0), 0)
        self.assertEqual(self.num.subtract(10, 5), 5)
        self.assertEqual(self.num.subtract(4, -3), 7)
        self.assertNotEqual(self.num.subtract(-5, -2), -7)
        self.assertEqual(self.num.subtract(-5.5, -2), -3.5)

    def test_multiply(self):
        self.assertEqual(self.num.multiply(1, 0), 0)
        self.assertEqual(self.num.multiply(2, 2), 4)
        self.assertEqual(self.num.multiply(10.5, -5), -52.5)
        self.assertEqual(self.num.multiply(-5, -2), 10)
        self.assertNotEqual(self.num.multiply(-2, -3), -6)

    def test_divide(self):
        self.assertEqual(self.num.divide(20, 10), 2)
        self.assertEqual(self.num.divide(-20.5, 10), -2.05)
        self.assertEqual(self.num.divide(-20, -5), 4)
        self.assertNotEqual(self.num.multiply(10, 5), -2)
        self.assertRaises(ZeroDivisionError, lambda: Calculator.divide(self, 1, 0))

    def test_evaluate(self):
        self.assertEqual(self.num.evaluate('2+3-2'), '3.0')
        self.assertEqual(self.num.evaluate('2*8/0.5'), '32.0')
        self.assertEqual(self.num.evaluate('1+2*3'), '7.0')
        self.assertNotEqual(self.num.evaluate('1+2*5'), 11.0)
        self.assertRaises(IndexError, lambda: Calculator.evaluate(self, ''))

    def test_evaluatepar(self):
        self.assertEqual(self.num.evaluatepar('(1/0.5+2)'), '4.0')
        self.assertEqual(self.num.evaluatepar('1+(1.2+2.3)'), '1+3.5')
        self.assertEqual(self.num.evaluatepar('5-((2+4)*2)'), '5-12.0')
        self.assertRaises(SyntaxError, lambda: Calculator.evaluatepar(self, '4+(4*25'))


if __name__ == '__main__':
    unittest.main()