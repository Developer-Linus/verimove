from django.shortcuts import render
from .serializers import AttendanceModelSerializer
from rest_framework import viewsets
from .models import AttendanceRecordModel

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset =AttendanceRecordModel.objects.all()
    serializer_class= AttendanceModelSerializer