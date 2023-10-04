from unittest import TestCase
from tdd_class.back_to_sender_logistics import calculate_riders_payment


class TestCaseForBackToSenderLogistics(TestCase):
    def test_calculate_riders_payment_one(self):
        payment = calculate_riders_payment(20)
        self.assertEqual(payment, 8200)
