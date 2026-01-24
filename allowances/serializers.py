from rest_framework import serializers
from .models import AllowanceModel

class AllowanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowanceModel
        fields = ["id","month","staff","total_amount", "status", "days_present", "rate_per_day"]
        read_only_fields = ("id", "staff", "days_present", "rate_per_day", "total_amount")