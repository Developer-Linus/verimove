from django.shortcuts import render
from rest_framework import viewsets
from .models import CheckInModel
from .serializers import CheckInModelSerializer

class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckInModel.objects.all()
    serializer_class = CheckInModelSerializer