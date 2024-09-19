from django.db import models
from wallet.models import Wallet


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Specialty(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=100)
