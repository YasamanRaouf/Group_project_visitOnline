from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    balance = models.PositiveIntegerField(default=0)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

    def transfer(self, recipient_wallet, amount):
        if self.withdraw(amount):
            recipient_wallet.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Wallet ID: {self.wallet_id} with balance {self.balance}"
