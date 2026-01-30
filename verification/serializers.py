from rest_framework import serializers

class GateCaptureSerializer(serializers.Serializer):
    plate_number = serializers.CharField(max_length=15)
    image = serializers.ImageField(required=False)