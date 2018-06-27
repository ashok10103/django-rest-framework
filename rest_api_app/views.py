from django.shortcuts import render
from rest_framework import generics,permissions
from .permissions import IsOwner
from .serializers import BucketListSerializer
from .models import BucketList

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
       
