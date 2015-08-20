from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


NOTIFICATION_TYPES = (
    ('e', _('Email')),
    ('s', _('SMS')),
)

class HappyBirthday(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True,
                                verbose_name=_('user'), related_name='happy_birthday')
    is_active = models.BooleanField(default=False)
    sms = models.CharField(_("text"), max_length=160, null=True, blank=True,
                           default="Happy $patients-age Birthday $patients-first-name!")
    email_subject =  models.CharField(_("subject"), max_length=77, null=True,
                                      blank=True, default="Happy Birthday $patients-first-name $patients-last-name!")
    email_body = models.TextField(_("body"), null=True, blank=True,
                                 default=
"""Hello $patients-first-name,

Just wanted to wish you a Happy $patients-age Birthday!

All the best,

-   Dr. $doctors-first-name $doctors-last-name $doctors-suffix

$doctors-job-title
Phone: $doctors-office-phone
Email: $doctors-email""")
    notification_type = models.CharField(_('notification method'), max_length=1,
                                        choices=NOTIFICATION_TYPES,
                                        default=NOTIFICATION_TYPES[0][0])
    last_ran = models.DateField(null=True, blank=True)
