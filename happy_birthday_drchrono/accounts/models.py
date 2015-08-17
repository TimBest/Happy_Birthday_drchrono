from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


PROFILE_TYPE_CHOICES = (
    ('f', _('Fan')),
    ('m', _('Musician')),
    ('v', _('Venue')),
)

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True,
                                verbose_name=_('user'), related_name='profile')

    def __unicode__(self):
        return '%s' % self.user.username

    def get_absolute_url(self):
		# TODO: change this to the appropriate profile URL
        return ('home')

    get_absolute_url = models.permalink(get_absolute_url)
