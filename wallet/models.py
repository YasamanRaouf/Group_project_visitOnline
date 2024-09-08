from django.db import models


from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"Wallet ID: {self.wallet_id} with balance {self.balance}"
