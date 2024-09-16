
from django.db import models
from django.contrib.auth.models import User

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



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    wallet_id = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.user.username
