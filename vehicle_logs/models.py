from django.db import models
from django.utils import timezone
from staffs.models import StaffModel

DIRECTION_CHOICES = [
    ('IN', 'IN'),
    ('OUT', 'OUT'),
]
class CheckInModel(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    staff_id = models.ForeignKey(StaffModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    gate = models.CharField(max_length=50)
    direction = models.CharField(max_length=3,choices=DIRECTION_CHOICES)
    image_part = models.CharField(max_length=100)
    def __str__(self)->str:
        return f"{self.plate_number} ({self.staff_id}) ({self.gate}) ({self.timestamp})"
    def save(self, *args, **kwargs):
        self.plate_number = self.plate_number.upper()
        super(CheckInModel, self).save(*args, **kwargs)