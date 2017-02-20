# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 03:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Session', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252, verbose_name='band name')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandmaker_band_master', to=settings.AUTH_USER_MODEL, verbose_name='band master')),
            ],
        ),
        migrations.CreateModel(
            name='MusicPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252, verbose_name='music name')),
                ('datetime', models.DateTimeField(verbose_name='perfome Date and time')),
                ('youtubeURL', models.URLField()),
                ('instruments', models.ManyToManyField(related_name='bandmaker_musicpiece_related', to='Session.Instrument', verbose_name='required instruments')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='musicPieces',
            field=models.ManyToManyField(related_name='bandmaker_band_musics', to='BandMaker.MusicPiece', verbose_name='band music list'),
        ),
        migrations.AddField(
            model_name='band',
            name='sessions',
            field=models.ManyToManyField(related_name='bandmaker_band_sessions', to='Session.Session', verbose_name='band session list'),
        ),
    ]