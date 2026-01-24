from rest_framework import serializers
from .models import VehicleModel

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ["id", "plate_number", "staff_id", "is_active", "created_at", "updated_at"]
        read_only_fields = ("id", "staff_id")