import unittest

from Excercises.function_odd import biggest_odd


class TestBiggestOdd(unittest.TestCase):

    def test_odd_largest_number(self):
        numbers = '23569'
        result = biggest_odd(numbers)
        self.assertEqual(result, 9)

