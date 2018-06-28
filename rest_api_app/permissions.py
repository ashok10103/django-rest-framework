from rest_framework.permissions import BasePermission

from .models import BucketList,DoctorList

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        if isinstance(obj, BucketList):
            return obj.owner == request.user       
        return obj.owner == request.user

    def has_object_permission(self, request, view, obj):

        if isinstance(obj, DoctorList):
            return obj.owner == request.user       
        return obj.owner == request.user