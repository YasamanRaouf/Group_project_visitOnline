from django.apps import AppConfig
from django.db.models.signals import post_save


class DoctorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor'

    def ready(self):
        from doctor.utils import send_confirmation_email



# class DoctorConfig(AppConfig):
#     name = 'doctor'

    # def ready(self):
    #     import doctor.emails
