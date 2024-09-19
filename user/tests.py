from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from doctor.models import Doctor  # از اپلیکیشن doctor وارد شده است
from django.contrib.auth.models import User
from user.forms import SignUpForm, LoginForm, UpdateUserForm, UpdateDoctorForm

UserModel = get_user_model()

class UserViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.edit_profile_url = reverse('edit_profile')
        self.edit_doctor_url = reverse('edit_doctor')
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='password123',
            full_name='Test User',
            phone_number='1234567890',
            wallet_id='wallet123',
            is_admin=False,
            email='testuser@example.com'
        )
        self.doctor = Doctor.objects.create(
            user=self.user,
            specialty='General',
            price=100
        )

    def test_signup_view(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'full_name': 'New User',
            'phone_number': '0987654321',
            'wallet_id': 'wallet456',
            'is_admin': False,
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # انتظار Redirect بعد از ثبت‌نام موفق
        self.assertTrue(UserModel.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # انتظار Redirect بعد از ورود موفق
        self.assertIn('_auth_user_id', self.client.session)  # بررسی ورود موفقیت‌آمیز

    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(self.edit_profile_url, {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'full_name': 'Updated User',
            'phone_number': '1111111111',
            'wallet_id': 'wallet789',
            'is_admin': True
        })
        self.assertEqual(response.status_code, 302)  # انتظار Redirect بعد از ویرایش موفق
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')

    def test_edit_doctor_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(self.edit_doctor_url, {
            'specialty': 'Cardiology',
            'price': 150,
            'saturday': '9am-5pm',
            'sunday': '10am-4pm',
            'monday': '9am-5pm',
            'tuesday': '9am-5pm',
            'wednesday': '9am-5pm',
            'thursday': '9am-5pm',
            'friday': '9am-5pm',
            'interval': 30
        })
        self.assertEqual(response.status_code, 302)  # انتظار Redirect بعد از ویرایش موفق
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.specialty, 'Cardiology')
        self.assertEqual(self.doctor.price, 150)

class UserFormsTests(TestCase):
    def test_signup_form_validity(self):
        form = SignUpForm(data={
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'full_name': 'Test User',
            'phone_number': '1234567890',
            'wallet_id': 'wallet123',
            'is_admin': False,
            'email': 'testuser@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_validity(self):
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertTrue(form.is_valid())

    def test_update_user_form_validity(self):
        form = UpdateUserForm(data={
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'full_name': 'Updated User',
            'phone_number': '1111111111',
            'wallet_id': 'wallet789',
            'is_admin': True
        }, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_update_doctor_form_validity(self):
        form = UpdateDoctorForm(data={
            'specialty': 'Cardiology',
            'price': 150,
            'saturday': '9am-5pm',
            'sunday': '10am-4pm',
            'monday': '9am-5pm',
            'tuesday': '9am-5pm',
            'wednesday': '9am-5pm',
            'thursday': '9am-5pm',
            'friday': '9am-5pm',
            'interval': 30
        }, instance=self.doctor)
        self.assertTrue(form.is_valid())
