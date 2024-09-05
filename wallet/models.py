from django.db import models


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
