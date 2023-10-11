from unittest import TestCase

from Practice.function_to_multiply_practice import multiply


class Test(TestCase):
    def test_multiply(self):
        result = multiply(5,2)
        self.assertEqual(result,10)
