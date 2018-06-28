from django.shortcuts import render
from rest_framework import generics,permissions
from .permissions import IsOwner
from .serializers import BucketListSerializer,DoctorListSerializer
from .models import BucketList,DoctorList

# Create your views here.


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
