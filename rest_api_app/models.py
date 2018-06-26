from django.db import models

# Create your models here.
class BucketList(models.Model):
    name = models.CharField(max_length=250,blank=False,unique=True)
    owner=models.ForeignKey('auth.User',related_name='bucket_lists',on_delete=models.CASCADE)
    date_created =  models.DateTimeField(auto_now_add=True)
    date_modified =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.name)
    
    