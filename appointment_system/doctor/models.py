from django.db import models


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    speciality = models.ForeignKey('user.Speciality', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
