# Generated by Django 2.0.6 on 2018-06-29 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0014_auto_20180629_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationmodel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='locationmodel',
            name='longitude',
        ),
    ]
