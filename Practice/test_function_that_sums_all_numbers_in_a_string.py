from unittest import TestCase

from Practice.function_that_sums_all_numbers_in_a_string import check_for_number


class Test(TestCase):
    def test_check_for_number(self):
        result = check_for_number('pretty melody1234')
        self.assertEqual(result,4)
