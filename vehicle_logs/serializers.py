from rest_framework import serializers
from .models import CheckInModel

class CheckInModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckInModel
        fields = ["id", "plate_number", "staff_id", "timestamp", "gate", "direction", "image_part"]
        read_only_fields = ("id","staff_id")