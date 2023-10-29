import unittest
from unittest import TestCase

from assignments.list_to_dictionary import list_to_dictionary

class TestListToDictionary(unittest.TestCase):
    def test_list_to_dictionary(self):
        my_list = [{'key': 'a', 'value': 'apple'},
                   {'key': 'b', 'value': 'banana'},
                   {'key': 'c', 'value': 'coconut'}]
        result_dict = list_to_dictionary(my_list, 'key', 'value')
        expected_dict = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(result_dict, expected_dict)