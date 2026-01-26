from rest_framework import serializers
from .models import AttendanceRecordModel

class AttendanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecordModel
        fields =["id","staff", "date", "first_checkin", "source" ]
        read_only_fields = ("id", "staff")