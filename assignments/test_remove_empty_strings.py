from unittest import TestCase

from assignments.remove_empty_strings import remove_empty_string


class Test(TestCase):
    def test_remove_empty_string(self):
        sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        new_list = remove_empty_string(sample_input)
        expected = ['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(expected,new_list)
