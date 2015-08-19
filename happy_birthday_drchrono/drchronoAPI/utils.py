import datetime

from drchronoAPI.api import get_patients
from drchronoAPI.models import Patient


def update_patients_for_user(user, last_ran=None):
    parameters = {}
    if last_ran:
        parameters['since'] = last_ran
    patients = get_patients(user, parameters)
    for p in patients:
        date_of_birth = p['date_of_birth']
        if date_of_birth:
            year, month, day = [int(x) for x in p['date_of_birth'].split('-')]
            date_of_birth = datetime.date(year, month, day)
            patient, created = Patient.objects.update_or_create(
                id=p['id'],
                defaults= {
                    'user': user,
                    'date_of_birth': date_of_birth,
                    'doctor': p['doctor'],
                    'first_name': p['first_name'],
                    'last_name': p['last_name'],
                    'cell_phone': p['cell_phone'],
                    'email': p['email'],
                    'state': p['state'],
                },
            )
