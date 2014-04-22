import unittest
from expression_generator import ExpressionGenerator


class TestExpressionGenerator(unittest.TestCase):
    def setUp(self):
        self.expr = ExpressionGenerator()
        self.expr._first_constant = 3
        self.expr._second_constant = 2
        self.expr._operator = '+'

    def test_get_value(self):
        result = self.expr.get_value()
        self.assertEqual(5, result)

    def test_generate_number(self):
        result = self.expr._generate_number() < 100\
            and self.expr._generate_number() >= 0

        self.assertTrue(result)

    def test_generate_operator(self):
        result = self.expr._generate_operator()\
            in self.expr._operators

        self.assertTrue(result)

    def test_calculate(self):
        result = self.expr._calculate()
        self.assertEqual(5, result)

    def test_to_string(self):
        result = str(self.expr)
        expected = "3 + 2"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()