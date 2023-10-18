from unittest import TestCase

from Practice.function_that_takes_two_strings import equal_strings


class Test(TestCase):
    def test_equal_strings(self):
        self.assertTrue(equal_strings('mel','lem'))

    def test_un_equal_strings(self):
        self.assertFalse(equal_strings('mel','girl'))