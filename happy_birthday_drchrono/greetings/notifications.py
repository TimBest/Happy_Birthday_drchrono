from celery.schedules import crontab
from celery.task import periodic_task

from greetings.models import HappyBirthday

@periodic_task(run_every=crontab(hour=9, minute=30, day_of_week="*"))
def send_happy_birthdays():
    sms_greetings = HappyBirthday.filter(notification_type="s", is_active=True)
    email_greetings = HappyBirthday.filter(notification_type="e",  is_active=True)

    for greeting in email_greetings:
        # query user's patients and if it is their birthday send them an email
        pass
    for greeting in sms_greetings:
        # query user's patients and if it is their birthday send them an sms
        pass
