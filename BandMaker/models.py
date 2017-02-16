from django.db import models
from Applicants.models import MyUser
from Session.models import Session, Instrument

# Create your models here.
class Band(models.Model):
    master = models.ForeignKey(
        MyUser,
        verbose_name='band master',
        related_name='%(app_label)s_%(class)s_master'
    )

    sessions = models.ManyToManyField(
        Session,
        verbose_name='band session list',
        related_name='%(app_label)s_%(class)s_sessions'
    )

    name = models.CharField(max_length=252, verbose_name='band name')

    musicPieces = models.ManyToManyField(
        Instrument,
        verbose_name='band music list',
        related_name='%(app_label)s_%(class)s_musics'
    )

class MusicPiece(models.Model):
    name = models.CharField(max_length=252, verbose_name='music name')

    datetime = models.DateTimeField(verbose_name='perfome Date and time')

    instruments = models.ManyToManyField(
        Instrument,
        verbose_name='required instruments',
        related_name='%(app_label)s_%(class)s_related'
    )

    youtubeURL = models.URLField()
