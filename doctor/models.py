from django.db import models
from django.conf import settings
from user.models import Specialty, User


class Doctor(models.Model):

    def availability_dict(
        saturday=None,
        sunday=None,
        monday=None,
        tuesday=None,
        wednesday=None,
        thursday=None,
        friday=None,
        interval=20,
    ):
        return {
            'saturday': [saturday] if saturday else [],
            'sunday': [sunday] if sunday else [],
            'monday': [monday] if monday else [],
            'tuesday': [tuesday] if tuesday else [],
            'wednesday': [wednesday] if wednesday else [],
            'thursday': [thursday] if thursday else [],
            'friday': [friday] if friday else [],
            'interval': interval,
        }

    doctor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    availability = models.JSONField(default=availability_dict())

    def __str__(self):
        return f"Dr. {self.user.full_name} - {self.specialty.spec_name}"

    def get_available_slots(self, day):
        return self.availability.get(day, [])


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Visit with Dr. {self.doctor.user.full_name} on {self.date_time}"
