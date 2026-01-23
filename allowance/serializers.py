from rest_framework import serializers
from .models import AllowanceModel

class AllowanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowanceModel
        fields = ["id","month","staff_id", "total_amount", "status", "source_log_id"]
        read_only_fields = ("id", "staff_id", "status")