# Generated by Django 2.0.6 on 2018-06-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0004_auto_20180627_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='feedback',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
