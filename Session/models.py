from django.db import models
from Applicants.models import MyUser

# Create your models here.
class Session(models.Model):
    players = models.ForeignKey(
        MyUser,
        verbose_name='own user info',
        related_name='%(app_label)s_%(class)s_related'
    )

    instruments = models.ManyToManyField(Instrument)

class Instrument(models.Model):
    name = models.CharField(max_length=50, verbose_name='instrument name')

