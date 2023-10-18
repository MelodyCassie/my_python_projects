from unittest import TestCase

from Excercises.higher_order import bigger_odd


class Test(TestCase):
    def test_bigger_odd(self):
        self.assertEqual(bigger_odd('23495'), 9)
