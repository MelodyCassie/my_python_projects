from unittest import TestCase

from Practice.compares_two_strings import equal_strings


class Test(TestCase):
    def test_equal_strings(self):
        self.assertTrue(equal_strings('love', 'evol'))

    def test_un_equal_strings(self):
        self.assertFalse(equal_strings('melody', 'babygirl'))