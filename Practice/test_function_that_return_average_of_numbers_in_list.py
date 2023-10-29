from unittest import TestCase

from Practice.function_that_return_average_of_numbers_in_list import calculate_average


class Test(TestCase):
    def test_calculate_average(self):
        result = calculate_average([1,2,3,4,5,6])
        self.assertEqual(3.5,result)
