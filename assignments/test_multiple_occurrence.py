from unittest import TestCase

from assignments.multiple_occurrence import filter_multiple_occurrence


class Test(TestCase):
    def test_filter_multiple_occurrence(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        multiple_occurence = filter_multiple_occurrence(sample_input)
        expected = [1, 2, 5]

        self.assertEqual(expected,multiple_occurence)
