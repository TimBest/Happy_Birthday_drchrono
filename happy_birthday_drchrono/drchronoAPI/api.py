import requests, urllib


def get_patients(user, parameters={}):
    social = user.social_auth.get(user=user)
    access_token = social.extra_data['access_token']
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    patients = []
    patients_url = 'https://drchrono.com/api/patients?' + urllib.urlencode(parameters)
    while patients_url:
        data = requests.get(patients_url, headers=headers).json()
        patients.extend(data['results'])
        patients_url = data['next'] # A JSON null on the last page
    return patients
