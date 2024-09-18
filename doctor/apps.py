from django.apps import AppConfig


class DoctorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor'


class DoctorConfig(AppConfig):
    name = 'doctor'

    def ready(self):
        from emails import send_confirmation_email
