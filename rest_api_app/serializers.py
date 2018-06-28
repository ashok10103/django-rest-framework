from rest_framework import serializers
from .models import BucketList,DoctorList

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
        fields = (
            'id',
            'clinic_name',
            'speciality',
            'feedback',
            'location',
            'doctor_fee',
            'available_days',
            'available_timing',
            'doctor_name',
            'rating_percentage',
            'votes',
            'images',
            'owner',
            )
        # read_only_fields = ('owner')

