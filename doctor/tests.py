from django.test import TestCase
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



# Create your tests here.
