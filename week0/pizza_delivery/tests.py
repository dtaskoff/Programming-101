# I'm not testing that..
import unittest
import solution


class TestPizzaDelivery (unittest.TestCase):
    def setUp(self):
        self.order = {"initial": 0.00}

    def test_take(self):
        result = solution.take("tester", 42.00, self.order)
        self.assertEqual("Taking order from tester for 42.00", result)
        self.assertEqual({"initial": 0.00, "tester": 42.00}, self.order)

    def test_status(self):
        result = solution.status(self.order)
        self.assertEqual(["initial - 0.00"], result)

    def test_format_output(self):
        result = solution.format_output("first", "second")
        self.assertEqual("first - second", result)

    #def test_save(self):
    #    result = solution.save(self.order)
    #    self.assertEqual("Order saved", result)

    def test_list(self):
        self.assertEqual(1, len(solution.list_()))

    def test_load(self):
        file_ = open("orders_0000_00_00_00_00_00", "w")
        file_.write("tester - 42.00")
        file_.close()
        result = solution.load(1, self.order)
        self.assertEqual({"tester": 42.00}, result)

    def test_help(self):
        self.assertEqual("List of possible commands: \n"\
            + "take <name> <price>\n"\
            + "status\n"\
            + "save\n"\
            + "list\n"\
            + "load <number>\n"\
            + "finish\n"\
            + "help\n",
            solution.help())

    def test_unknown(self):
        self.assertEqual("Unknown command.\n"\
            + "Try entering help for further information.",
            solution.unknown())

if __name__ == '__main__':
    unittest.main()