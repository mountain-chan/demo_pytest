import unittest


def sum(x, y):
    return x + y


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertNotEqual(sum(1, 1), 5)

    def test_sum_2(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertNotEqual(sum(1, 1), 5)

    def test_sum_3(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertNotEqual(sum(1, 1), 5)


if __name__ == "__main__":
    MyTestCase()
