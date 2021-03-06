# Generated by Django 2.0.6 on 2018-06-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_auto_20180626_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=250, null=True)),
                ('doctor_name', models.CharField(max_length=250, null=True)),
                ('speciality', models.CharField(max_length=450, null=True)),
                ('feedback', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=500, null=True)),
                ('doctor_fee', models.CharField(max_length=4, null=True)),
                ('available_days', models.CharField(max_length=50, null=True)),
                ('available_timing', models.CharField(max_length=50, null=True)),
                ('rating_percentage', models.CharField(max_length=10, null=True)),
                ('votes', models.CharField(max_length=4, null=True)),
                ('images', models.ImageField(upload_to='doctor_profile/')),
            ],
        ),
    ]
