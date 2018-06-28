from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models
# Create your models here.
class BucketList(models.Model):
    name = models.CharField(max_length=250,blank=False,unique=True)
    owner=models.ForeignKey('auth.User',related_name='bucket_lists',on_delete=models.CASCADE,null=True)
    date_created =  models.DateTimeField(auto_now_add=True)
    date_modified =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class DoctorList(models.Model):
    clinic_name = models.CharField(max_length=250,blank=False,null=True)
    owner=models.ForeignKey('auth.User',related_name='doctor_lists',on_delete=models.CASCADE,null=True)    
    doctor_name = models.CharField(max_length=250,blank=False,null=True)
    speciality = models.CharField(max_length=450,blank=False,null=True)
    feedback = models.CharField(max_length=20,blank=False,null=True)
    location = models.CharField(max_length=500,blank=False,null=True)
    doctor_fee = models.CharField(max_length=4,blank=False,null=True)
    available_days = models.CharField(max_length=50,blank=False,null=True)
    available_timing = models.CharField(max_length=50,blank=False,null=True)
    rating_percentage = models.CharField(max_length=10,blank=False,null=True)
    votes = models.CharField(max_length=4,blank=False,null=True)
    images = models.CharField(max_length=500,blank=True,null=True) 
    location = models.CharField(max_length=500,blank=False,null=True)
    location_coords = gis_models.PointField(max_length=500,blank=False,null=True)   
    objects = GeoManager()


    class Meta:
        verbose_name_plural = "DoctorsList"    

    def __str__(self):
        return self.doctor_name
    



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
    