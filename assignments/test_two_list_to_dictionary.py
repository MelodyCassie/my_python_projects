import unittest
from unittest import TestCase

from assignments.two_list_to_dictionary import two_list_to_dictionary


class Test(TestCase):
    def test_two_list_to_dictionary(self):
        class TestCombineListToDictionary(unittest.TestCase):
            def test_two_list_to_dictionary(self):
                my_list_one = ['a', 'b', 'c', 'd', 'e']
                my_list_two = [1, 2, 3, 4, 5]
                combined_list_to_dictionary = two_list_to_dictionary(my_list_one, my_list_two)
                expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
                self.assertEqual(combined_list_to_dictionary, expected)

