from rest_framework import serializers
from .models import BucketList,DoctorList
from django.contrib.gis.geos import Point


class BucketListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    
    
    class Meta:
        model =BucketList
        fields = ('id','name', 'owner','date_created','date_modified')
        read_only_fields = ('date_created','date_modified')


class DoctorListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model =DoctorList
        fields = '__all__'

   
     
   


