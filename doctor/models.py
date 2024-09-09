from django.db import models

class Doctor(models.Model):

    availability_dict = {
        'saturday': [],
        'sunday': [],
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'interval': 20,
    }

    doctor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    specialty = models.ForeignKey('user.Specialty', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    availability = models.JSONField(default=availability_dict)

    def __str__(self):
        return f"Dr. {self.user.full_name} - {self.specialty.spec_name}"

    def get_available_slots(self, day):
        # Return available slots for a specific day
        return self.availability.get(day, [])
