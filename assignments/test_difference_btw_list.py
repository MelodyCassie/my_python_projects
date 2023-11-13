from unittest import TestCase

from assignments.difference_btw_list import difference_of_list


class test_difference_of_list(TestCase):
    def test_difference_of_list(self):
        my_list_tuple = [10,75,20,30,15,5,40,25,40,35]
        result_of_difference = difference_of_list(my_list_tuple)
        self.assertEqual(70,result_of_difference)
