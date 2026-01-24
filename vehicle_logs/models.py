from django.db import models
from staffs.models import StaffModel

DIRECTION_CHOICES = [
    ('IN', 'IN'),
    ('OUT', 'OUT'),
]
class CheckInModel(models.Model):
    plate_number = models.CharField(max_length=10)
    vehicle = models.ForeignKey("vehicles.VehicleModel", null=True, blank=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey("staffs.StaffModel", null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    gate = models.CharField(max_length=50)
    direction = models.CharField(max_length=3,choices=DIRECTION_CHOICES)
    image = models.ImageField(upload_to="vehicle_logs/%Y/%m/%d/", null=True, blank=True)
    def __str__(self)->str:
        return f"{self.plate_number} ({self.staff_id}) ({self.gate}) ({self.timestamp})"
    def save(self, *args, **kwargs):
        self.plate_number = self.plate_number.upper()
        super(CheckInModel, self).save(*args, **kwargs)