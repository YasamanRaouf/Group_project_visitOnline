from django.test import TestCase
from user.models import Specialty, User
from django.utils import timezone
from model_bakery import baker
from visitonline.doctor.models import Doctor
from django.contrib.auth.models import User
from django.urls import reverse

class DoctorTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User, username='testuser', password='testpassword')
        self.doctor = baker.make(Doctor, uuser=self.user ,specialty='testspecialty')

    def tearDown(self) -> None:
        self.user.delete()
        self.doctor.delete()

    def test_doctor_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('Doctor_list'))  

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor/templates/doctorList.html')
        self.assertContains(response, self.user.username)

    def test_doctor_search_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('Doctor_Search') + '?search_item=Cardiology')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor/templates/doctorSearch.html')
        self.assertContains(response, self.user.username)

    def test_doctor_search_view_no_results(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('Doctor_Search') + '?search_item=NonExistentSpecialty')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor/templates/doctorSearch.html')
        self.assertContains(response, 'No doctors found')


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
