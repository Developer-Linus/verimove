from django.shortcuts import render
from .serializers import StaffModelSerializer
from rest_framework import viewsets
from .models import StaffModel

class StaffViewSet(viewsets.ModelViewSet):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializer