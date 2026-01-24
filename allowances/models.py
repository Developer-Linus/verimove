from django.db import models
from staffs.models import StaffModel
from vehicle_logs.models import CheckInModel
from datetime import date

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('FAILED', 'Failed'),
]
class AllowanceModel(models.Model):
    month = models.DateField(help_text="Use first day of month, e.g. 2026-01-01", db_index=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name="allowances")
    days_present = models.PositiveIntegerField(default=0)
    rate_per_day = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["staff", "month"], name="uniq_staff_month_allowance")
        ]
        ordering = ["-month"]

    def __str__(self) -> str:
        return f"{self.staff.staff_number} {self.month:%Y-%m} {self.total_amount}"
    
    def save(self, *args, **kwargs):
       
        if self.month:
            # Normalize to first day of the month
            self.month = self.month.replace(day=1)

        # Always compute total automatically
        self.total_amount = (self.days_present or 0) * (self.rate_per_day or 0)

        super().save(*args, **kwargs)