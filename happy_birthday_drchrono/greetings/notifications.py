import datetime
from celery.schedules import crontab
from celery.task import periodic_task

from drchronoAPI.utils import update_patients_for_user, update_doctors_for_user
from drchronoAPI.models import Doctor
from greetings.messages import send_email, send_sms
from greetings.models import HappyBirthday
from utils.functions import get_object_or_None


"""
    TODO: Imporve by running every hour.
    Filter patients by those are in the where it is currently 9:30am (use the state field).
"""
@periodic_task(run_every=crontab(hour=9, minute=30, day_of_week="*"))
def send_happy_birthdays():
    sms_greetings = HappyBirthday.objects.filter(notification_type="s", is_active=True)
    email_greetings = HappyBirthday.objects.filter(notification_type="e",  is_active=True)
    today = datetime.datetime.now().today()

    for greeting in email_greetings:
        update_doctors_for_user(greeting.user)
        update_patients_for_user(greeting.user)#, greeting.last_ran)

        for patient in greeting.user.patients.filter(date_of_birth__month=today.month, date_of_birth__day=today.day):
            if patient.email:
                send_email(
                    evalualte_variables(patient, greeting.email_subject),
                    evalualte_variables(patient, greeting.email_body),
                    [patient.email,]
                )

    for greeting in sms_greetings:
        update_doctors_for_user(greeting.user)
        update_patients_for_user(greeting.user, greeting.last_ran)

        for patient in greeting.user.patients.filter(date_of_birth__month=today.month, date_of_birth__day=today.day):
            if patient.cell_phone:
                send_sms(
                    evalualte_variables(patient, greeting.sms),
                    patient.cell_phone
                )
    greeting.last_ran = today
    greeting.save()

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def evalualte_variables(patient, message=''):
    age = ord(datetime.datetime.now().today().year - patient.date_of_birth.year)
    variables = {
        "$patients-first-name": patient.first_name,
        "$patients-last-name": patient.last_name,
        "$patients-age": age,
    }
    doctor = get_object_or_None(Doctor, id=patient.doctor)
    if doctor:
        variables.update({
            "$doctors-first-name": doctor.first_name,
            "$doctors-last-name": doctor.last_name,
            "$doctors-suffix": doctor.suffix,
            "$doctors-job-title": doctor.job_title,
            "$doctors-specialty": doctor.specialty,
            "$doctors-cell-phone": doctor.cell_phone,
            "$doctors-home-phone": doctor.home_phone,
            "$doctors-office-phone": doctor.office_phone,
            "$doctors-email": doctor.email,
            "$doctors-website": doctor.website,
        })


    message_parts = message.split('\$')
    for i in range(len(message_parts)):
        for variable, value in variables.iteritems():
            message_parts[i] = message_parts[i].replace(variable, value)
    return '$'.join(message_parts)
