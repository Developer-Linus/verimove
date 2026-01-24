from django.shortcuts import render
from .models import VehicleModel
from .serializers import VehicleModelSerializer
from rest_framework import viewsets

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
