import unittest
from solution import count_words


class CountWordsTest(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual({ "apple": 2, "banana": 1, "pie": 1 },
            count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual({ "python": 3, "ruby": 1 },
            count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    unittest.main()