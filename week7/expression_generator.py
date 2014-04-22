from random import randint


class ExpressionGenerator():
    _operators = ['+', '-', '*', '%', '/']

    def __init__(self):
        self.generate_new()

    def __str__(self):
        return "{} {} {}".format(self._first_constant,
            self._operator, self._second_constant)

    def get_value(self):
        return self._calculate()

    def generate_new(self):
        self._first_constant = self._generate_number()
        self._second_constant = self._generate_number()
        self._operator = self._generate_operator()

    def _generate_number(self):
        return randint(0, 99)

    def _generate_operator(self):
        rand = randint(0, len(self._operators) - 1)
        return self._operators[rand]

    def _calculate(self):
        return eval(str(self))