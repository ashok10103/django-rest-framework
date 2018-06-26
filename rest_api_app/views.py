from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList
# Create your views here.


class HomeView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self,serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
       queryset = BucketList.objects.all()
       serializer_class = BucketListSerializer
