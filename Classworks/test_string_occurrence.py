import unittest
from unittest import TestCase

from Classworks.string_occurrence import replace_first_char, sample_string


class TestReplaceFirstChar(unittest.TestCase):

    def test_replace_first_char_no_replacement(self):
        input_string = 'restart'
        expected_result = 'resta$t'
        result = replace_first_char(input_string)
        self.assertEqual(result, expected_result)

    def test_replace_first_char_with_replacement(self):
        input_string = 'restart'
        expected_result = 'resta$t'
        result = replace_first_char(input_string)
        self.assertEqual(result, expected_result)
