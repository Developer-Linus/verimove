from django.shortcuts import render
from .serializers import AllowanceModelSerializer
from rest_framework import viewsets
from .models import AllowanceModel

class AllowanceViewSet(viewsets.ModelViewSet):
    queryset = AllowanceModel.objects.all()
    serializer_class = AllowanceModelSerializer