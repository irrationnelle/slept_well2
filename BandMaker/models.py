from django.db import models
from Applicants.models import MyUser

# Create your models here.
class Band(models.Model):
    master = models.ForeignKey(MyUser, verbose_name='band master', related_name='band')
    # members = models.ForeignKey(MyUser, verbose_name="session members", related_name='members')