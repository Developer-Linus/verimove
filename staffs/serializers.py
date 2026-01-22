from rest_framework import serializers
from .models import StaffModel

class StaffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = ["id","staff_number","full_name", "department", "role", "is_active", "is_allowance_legible"]
        read_only_fields = ("id", "staff_number", "full_name")