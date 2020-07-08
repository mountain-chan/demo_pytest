def add(x, y):
    return x + y


def test_add():
    assert add(5, 10) == 15
    assert add(-1, 1) == 0


def sum(x, y):
    return x + y


def test_sum():
    assert sum(2, 3) == 5  # Should be 5
    assert sum(1, 1) == 5  # Should be 2


if __name__ == "__main__":
    test_sum()

import unittest


def sum(x, y):
    return x + y


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertNotEqual(sum(1, 1), 5)


if __name__ == "__main__":
    MyTestCase()

