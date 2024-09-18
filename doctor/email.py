from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Visit


@receiver(post_save, sender=Visit)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        doctor = instance.doctor
        subject = 'Appointment Confirmation'
        message = f'Dear {user.first_name},\n\n' \
                  f'Your appointment with Dr. {doctor.user.full_name} on {instance.date_time} has been confirmed.\n\n' \
                  f'Thank you for booking with us.\n\n' \
                  f'Best regards,\nThe Team'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email

        send_mail(subject, message, from_email, [to_email])
