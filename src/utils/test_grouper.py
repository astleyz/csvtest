import unittest
from grouper import grouper


class TestGrouper(unittest.TestCase):
    """
    Test grouper
    """

    def test_grouper_with_exact_groups(self):
        iterable = [1, 2, 3, 4, 5, 6]
        result = list(grouper(iterable, 2))
        expected = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(result, expected)

    def test_grouper_with_fillvalue(self):
        iterable = [1, 2, 3, 4, 5]
        result = list(grouper(iterable, 3, fillvalue=0))
        expected = [(1, 2, 3), (4, 5, 0)]
        self.assertEqual(result, expected)

    def test_grouper_with_less_elements(self):
        iterable = [1, 2, 3]
        result = list(grouper(iterable, 2))
        expected = [(1, 2), (3, None)]
        self.assertEqual(result, expected)

    def test_grouper_with_empty_iterable(self):
        iterable = []
        result = list(grouper(iterable, 2))
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
