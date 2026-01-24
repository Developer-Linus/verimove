from django.db import models
from django.utils import timezone
from staffs.models import StaffModel

class VehicleModel(models.Model):
    plate_number= models.CharField(max_length=10, unique=True)
    staff_id = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name="vehicles")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self)->str:
        return f"{self.plate_number} ({self.staff_id})"
    def save(self, *args, **kwargs):
        self.plate_number = self.plate_number.upper()
        super(VehicleModel, self).save(*args, **kwargs)