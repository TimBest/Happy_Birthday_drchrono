from django.contrib.gis.db import models


# TODO: move timezone into its own app
class State(models.Model):
    state = models.CharField(max_length=2, unique=True, primary_key=True,)
    timezone = models.CharField(max_length=4, default="PST")
