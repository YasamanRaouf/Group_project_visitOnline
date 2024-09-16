from django.test import TestCase
from .models import Wallet


class WalletModelTests(TestCase):

    def setUp(self):
        self.wallet1 = Wallet.objects.create(balance=100)
        self.wallet2 = Wallet.objects.create(balance=50)

    def test_deposit(self):
        self.wallet1.deposit(50)
        self.assertEqual(self.wallet1.balance, 150)

    def test_withdraw(self):
        self.wallet1.withdraw(30)
        self.assertEqual(self.wallet1.balance, 70)

    def test_transfer(self):
        success = self.wallet1.transfer(self.wallet2, 40)
        self.assertTrue(success)
        self.assertEqual(self.wallet1.balance, 60)
        self.assertEqual(self.wallet2.balance, 90)
