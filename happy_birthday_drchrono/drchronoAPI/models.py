from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Patient(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True,)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='patients')
    date_of_birth = models.DateField(null=True)
    doctor = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    email = models.EmailField()
    state = models.CharField(max_length=255)
