from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    wallet = models.ForeignKey('wallet.Wallet', on_delete=models.CASCADE)
    email = models.EmailField()


class Specialty(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=100)
