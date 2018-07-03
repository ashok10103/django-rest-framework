from django.shortcuts import render
from rest_framework import generics,permissions
from .permissions import IsOwner
from .serializers import BucketListSerializer,DoctorListSerializer

from .models import BucketList,DoctorList

from django.views.generic import TemplateView
from django.template.context_processors import csrf

from django.core.serializers import serialize
from django.http import  HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class HomeView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
       queryset = BucketList.objects.all()
       serializer_class = BucketListSerializer
       permission_classes = (permissions.IsAuthenticated, IsOwner)

class DoctorListView(generics.ListCreateAPIView):
    queryset = DoctorList.objects.all()
    serializer_class = DoctorListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class DoctorListDetailsView(generics.RetrieveUpdateDestroyAPIView):
       queryset = DoctorList.objects.all()
       serializer_class = DoctorListSerializer
       permission_classes = (permissions.IsAuthenticated, IsOwner)

def get_data(request):
        
    lat = float(request.GET.get('latitude'))
    lng =float(request.GET.get('longitude'))     
    radius = int(request.GET.get('radius'))         
    point = Point(lng,lat)
    data = serialize('geojson',DoctorList.objects.filter(location_coords__distance_lte=(point, Distance(km=radius)))) 
    # data = serialize('geojson',DoctorList.objects.all())      
    return HttpResponse(data,content_type='json')



