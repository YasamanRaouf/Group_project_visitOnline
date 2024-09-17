from django.test import TestCase
from django.contrib.auth.models import User
from .models import Doctor
from user.models import Specialty, User
from django.utils import timezone
import json


class DoctorModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', first_name='Test', last_name='User')
        self.specialty = Specialty.objects.create(spec_name='Cardiology')

        self.doctor = Doctor.objects.create(
            user=self.user,
            specialty=self.specialty,
            price=100.00,
            is_active=True,
            availability={
                'monday': ['09:00', '10:00'],
                'tuesday': ['11:00', '12:00'],
                'interval': 20
            }
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.user, self.user)
        self.assertEqual(self.doctor.specialty, self.specialty)
        self.assertEqual(self.doctor.price, 100.00)
        self.assertTrue(self.doctor.is_active)
        self.assertEqual(self.doctor.availability,
                         self.doctor.availability_dict(
                             monday=['09:00', '10:00'],
                             tuesday=['11:00', '12:00'],
                             interval=20
                         )
                         )

    def test_get_available_slots(self):
        available_slots_monday = self.doctor.get_available_slots('monday')
        self.assertEqual(available_slots_monday, ['09:00', '10:00'])
        available_slots_tuesday = self.doctor.get_available_slots('tuesday')
        self.assertEqual(available_slots_tuesday, ['11:00', '12:00'])

    def test_book_appointment(self):
        day = 'monday'
        time_to_book = '09:00'
        if time_to_book in self.doctor.get_available_slots(day):
            self.doctor.availability[day].remove(time_to_book)
            self.doctor.save()
            self.assertNotIn(
                time_to_book, self.doctor.get_available_slots(day))
        else:
            self.fail("Time slot is not available for booking.")
