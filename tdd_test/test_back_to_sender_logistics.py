from unittest import TestCase
from tdd_class.back_to_sender_logistics import calculate_riders_payment


class TestCaseForBackToSenderLogistics(TestCase):
    def test_calculate_riders_payment_one(self):
        payment = calculate_riders_payment(20)
        self.assertEqual(payment, 8200)


class TestCaseForBackToSenderLogistics(TestCase):
    def test_calculate_riders_payment_two(self):
        payment = calculate_riders_payment(55)
        self.assertEqual(payment, 9000)


class TestCaseForBackToSenderLogistics(TestCase):
    def test_calculate_riders_payment_three(self):
        payment = calculate_riders_payment(63)
        self.assertEqual(payment, 20750)


class TestCaseForBackToSenderLogistics(TestCase):
    def test_calculate_riders_payment_three(self):
        payment = calculate_riders_payment(88)
        self.assertEqual(payment, 49000)


