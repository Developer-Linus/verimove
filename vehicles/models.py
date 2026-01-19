from django.db import models
from django.utils import timezone
from staffs.models import StaffModel

class VehicleModel(models.Model):
    plate_number= models.CharField(max_length=10)
    staff_id = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name="vehicles")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self)->str:
        return f"{self.plate_number} ({self.staff_id})"