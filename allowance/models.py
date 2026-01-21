from django.db import models
from django.utils import timezone
from staffs.models import StaffModel
from vehicle_logs.models import CheckInModel

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('FAILED', 'Failed'),
]
class AllowanceModel(models.Model):
    month = models.CharField(max_length=100)
    staff_id = models.ForeignKey(StaffModel, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    source_log_id = models.ForeignKey(CheckInModel, on_delete=models.CASCADE)
    def __str__(self)->str:
        return f"{self.month} ({self.staff_id}) ({self.total_amount})"