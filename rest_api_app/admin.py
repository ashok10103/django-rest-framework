from django.contrib import admin
from rest_api_app.models import BucketList,DoctorList
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class DoctorListAdmin(LeafletGeoAdmin):
    list_display = ('doctor_name','speciality','location')
    # pass

admin.site.register(BucketList)
admin.site.register(DoctorList,DoctorListAdmin)
