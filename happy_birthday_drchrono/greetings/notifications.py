import datetime
from celery.schedules import crontab
from celery.task import periodic_task

from drchronoAPI.utils import update_patients_for_user
from greetings.messages import send_email, send_sms
from greetings.models import HappyBirthday


"""
    TODO: Imporve by running every hour.
    Filter patients by those are in the where it is currently 9:30am (use the state field).
"""
@periodic_task(run_every=crontab(hour=9, minute=30, day_of_week="*"))
def send_happy_birthdays():
    sms_greetings = HappyBirthday.objects.filter(notification_type="s", is_active=True)
    email_greetings = HappyBirthday.objects.filter(notification_type="e",  is_active=True)

    for greeting in email_greetings:
        update_patients_for_user(greeting.user, greeting.last_ran)
        today = datetime.datetime.now().today()

        for patient in greeting.user.patients.filter(date_of_birth__month=today.month, date_of_birth__day=today.day):
            if patient.email:
                send_email(greeting.email_subject, greeting.email_body, [patient.email,])

    for greeting in sms_greetings:
        update_patients_for_user(greeting.user, greeting.last_ran)
        today = datetime.datetime.now().today()

        for patient in greeting.user.patients.filter(date_of_birth__month=today.month, date_of_birth__day=today.day):
            if patient.email:
                send_sms(greeting.sms, patient.cell_phone)
