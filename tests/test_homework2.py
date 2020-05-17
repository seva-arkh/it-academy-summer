import ddt
import unittest


from src.homework2.task1 import total_sum


@ddt.ddt
class TestHomework2(unittest.TestCase):

    @ddt.data(
        (10, 33, 400, '4132 rubles 0 kopecks'),
        (50, 50, 50, '2525 rubles 0 kopecks'),
        (23, 36, 111, '2592 rubles 96 kopecks'),
        (535, 14, 543, '290581 rubles 2 kopecks'),
        (0, 0, 543, '0 rubles 0 kopecks'),
        (12, 12, 0, '0 rubles 0 kopecks'),
        (1, 0, 5, '5 rubles 0 kopecks'),
        (0, 5, 5, '0 rubles 25 kopecks'),
    )
    @ddt.unpack
    def test_task1(self, m, n, s, expected):
        """Task1. Roubles: {}, kopecks: {}, number: {}"""
        self.assertEqual(total_sum(m, n, s), expected)


if __name__ == '__main__':
    unittest.main()
