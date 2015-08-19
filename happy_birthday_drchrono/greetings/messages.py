from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, recipient_list):
    """Compose and send an email."""
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    # during the development phase, consider using the setting: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=True)


def send_sms(text, reciver, sender=None):
    # dummy function to act as a text message service
    pass
